# ------------
#                   O v e r v i e w 
# This is the complex microservice for canceling an order in the Shipper's UI
# =======================================
# ------    C o m p o n e n t s
# --- order.py
# --- email_test.py
# --- send_sms.py
# --- shipper.py
# --- activity.py

# ------    P r o c e d u r e
# 1-- The microservice receives an order cancelation form with ShipperID, receiver info {name, address, phone, email} 
# 2-- The microservice then cancels the order by calling order api via [POST]
# 3-- Activity Log is called for order cancelation
# 4-- Shipper's email is obtained through the Shipper microservice
# 5-- Shipper is emailed via Email microservice -AMQP-> sendgrid
# 6-- Receiver is notified via SMS microservice -AMQP-> Twilio
# =======================================

#   Imports
# ------------
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

# URLs to call
order_URL = "http://localhost:5000/order"
activity_URL = "http://localhost:5001/activity"
shipper_URL = "http://localhost:5002/shipper"
email_URL = "http://localhost:9000/email"
sms_URL = "http://localhost:5566/update"


@app.route("/cancel_order", methods=['POST'])
def cancel_order():

    if request.is_json:
        try:
            trackingID = request.get_json()
            print("\nReceived a tracking_id in JSON:", trackingID)
            result = processCancelOrder(trackingID)
            return jsonify(result), result["code"]

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "cancel_order.py internal error: " + ex_str
            }), 500

        # if reached here, not a JSON request.
        return jsonify({
            "code": 400,
            "message": "Invalid JSON input: " + str(request.get_data())
        }), 400


def processCancelOrder(trackingID):
    # 1. Send the order info (all params) into order microservice
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    order_result = invoke_http(order_URL, method='POST', json=order)
    print('order_result:', order_result)
        
    # 2. Cancel order in activity log
    # Create the activity log for canceled order
    code=order_result["code"]
    info_json=order_result['data']
    info=json.loads(info_json)
    tracking_id=info.trackingID
    if code in range(200, 300):
        message = jsonify(
            {
                "code":200,
                "data":{
                    "activity_id": None,
                    "tracking_id": tracking_id,
                    "timestamp": datetime.now(),
                    "delivery_status": "Order canceled",
                    "delivery_desc": "Order has been canceled by the shipper"
                    }
            }
        )
        print('\n\n-----Publishing the (canceled order info) message with routing_key=order.info-----')        
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="new.order", 
            body=message)
        print("\nCanceled Order published to RabbitMQ Exchange.\n")
    else:
        return jsonify(
            {
                "code": 500,
                "data":{
                    "tracking_id":tracking_id
                    },
                "message": "An error occurred while trying to cancel the order. "
            }
        ), 500
   
    # 3. Retrieve shipper Email
    shipperID=info.shipperID
    shipper_URL+='/'+shipperID
    email_result=invoke_http(shipper_URL, method="GET",json=None)  
    if code in range(200, 300):
        info_email_json=email_result["data"]
        info_email=json.loads(info_email_json)
        shipper_email=info_email.shipperEmail
        # if error is thrown, append to error_msg
    else:
        return jsonify(
            {
                "code": 500,
                "data":{
                    "email":email_result
                    },
                "message": "An error occurred while retrieving shipper email. "
            }
        ), 500

    # 4. Email shipper
    email_content="This is to inform you that Tracking ID: " +tracking_id+" has been successfully canceled"
    message=jsonify(
        {
            "toEmail":shipper_email,
            "subject":"Order has been canceled",
            "msg":email_content
        }
    )
    # Replace with this after AMQP has been set up
    # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="new.email", 
    #         body=message)

    # 5. Inform receiver
    recipient=info.receiverPhone
    msg="[Camel Couriers] Your order "+tracking_id+" has been canceled."
    sms_message=jsonify(
        {
            "toPhone":recipient,
            "content":msg
        }
    )
    sms_status=invoke_http(sms_URL, method="POST", json=sms_message)
    print(sms_status)

    # 6. Return cancled order as a json object with codes
    return order_result

# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for canceling an order...")
    app.run(host="0.0.0.0", port=5008, debug=True)
