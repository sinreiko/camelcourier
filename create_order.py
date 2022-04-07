# ------------
#                   O v e r v i e w
# This is the complex microservice for creating an order in the Shipper's UI
# =======================================
# ------    C o m p o n e n t s
# --- order.py
# --- email_test.py
# --- send_sms.py
# --- shipper.py
# --- activity.py

# ------    P r o c e d u r e
# 1-- The microservice receives an order form with ShipperID, receiver info {name, address, phone, email}
# 2-- The microservice then creates a new order by calling order api via [POST]
# 3-- Activity Log is called for order creation
# 4-- Shipper's email is obtained through the Shipper microservice
# 5-- Shipper is emailed via Email microservice -AMQP-> sendgrid
# 6-- Receiver is notified via SMS microservice -AMQP-> Twilio
# =======================================

#   Imports
# ------------
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
import os
import sys
from os import environ

import requests
from invokes import invoke_http
import amqp_setup
import pika

app = Flask(__name__)
CORS(app)

# [TO REPLACE] URLs to call
order_URL = environ.get('order_URL') or "http://localhost:5000/order"
# activity_URL = "http://localhost:5001/activity"
shipper_URL = environ.get('shipper_URL') or "http://localhost:5002/shipper"
# email_URL = "http://localhost:9000/email"
# sms_URL = "http://localhost:5566/update"


@app.route("/create_order", methods=['POST'])
def place_order():
    '''
        Takes in POST inputs for json object order with the following:
            - shipperID
            - receiverName
            - receiverAddress
            - receiverPhone
            - receiverEmail
            - pickupAddress
        and runs the procedure above (line 13-18)
    '''
    # Check input format and data of the request are JSON
    if request.is_json:
        try:
            order = request.get_json()
            print("\nReceived an order in JSON:", order)
            result = processCreateOrder(order)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + \
                fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "create_order.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processCreateOrder(order):
    # 1. Send the order info (all params) into order microservice
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    print('\n---order---', order)
    order_result = invoke_http(order_URL, method='POST', json=order)
    print('order_result:', order_result)
    # 2. Create order in activity log
    # create the activity log
    code = order_result["code"]

    if code in range(200, 300):
        info = order_result["data"]
        tracking_id = info["trackingID"]
        print('\n=============trackingID is: ', tracking_id)
        now = datetime.now()
        msg = {
            "code": 201,
            "data": {
                "activity_id": None,
                "tracking_id": tracking_id,
                "timestamp": now.strftime("%m-%d-%Y, %H:%M:%S"),
                "delivery_status": "Order created",
                "delivery_desc": "Order has been created by shipper"
            }
        }
        message = json.dumps(msg)
        print(
            '\n\n-----Publishing the (order info) message with routing_key=order.info-----')
        print("\n========= message check =========\n", message)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="new.order",
                                         body=message, properties=pika.BasicProperties(delivery_mode=2))

        print("\nOrder published to RabbitMQ Exchange.\n")
    else:
        print('\nFailed to create order')
        return{
            "code": 500,
            "message": "An error occurred while creating order. "
        }
    # 4. Retrieve shipper Email
    shipperID = info["shipperID"]
    shipperURL = shipper_URL+'/'+str(shipperID)
    shipper_result = invoke_http(shipperURL, method="GET", json=None)
    code = shipper_result["code"]
    print("\n========shipper result code is: =======\n", code)
    if code in range(200, 300):
        shipper = shipper_result["data"]
        print("\n========shipper result data is: =======\n",
              shipper_result['data'])
        shipper_email = shipper["shipperEmail"]
        email_content = "This is to inform you that Tracking ID: " + \
            str(tracking_id)+" has been successfully created"
    else:
        return{
            "code": 500,
            "data": {"email": shipper_result},
            "message": "An error occurred while retrieving shipper email. "
        }
    # # 5. Email shipper

    msg = {
        "toEmail": shipper_email,
        "subject": "New order has been created",
        "content": email_content
    }
    message = json.dumps(msg)
    print("\n====email message=====\n", message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="new.email",
                                     body=message, properties=pika.BasicProperties(delivery_mode=2))
    print("\n----- email microservice end ------")
    # 6. Inform receiver
    recipient = info["receiverPhone"]
    msg = "[Camel Couriers] Your order "+str(tracking_id)+" has been created."

    sms_msg = {
        "toPhone": recipient,
        "content": msg
    }
    message = json.dumps(sms_msg)
    print("\n=====sms_msg: ========\n", message)
    # sms_status=invoke_http(sms_URL, method="POST", json=sms_message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="new.sms",
                                     body=message, properties=pika.BasicProperties(delivery_mode=2))
    # print(sms_status)
    # 7. Return created order as a json object with codes
    return order_result


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for creating an order...")
    app.run(host="0.0.0.0", port=5007, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
