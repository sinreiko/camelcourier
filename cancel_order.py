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
from email import message
from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

import os
import sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

# URL of all the simple microservices that you're contacting
order_URL = environ.get('order_URL') or "http://localhost:5000/order"
shipper_URL = environ.get('shipper_URL') or "http://localhost:5002/shipper"


@app.route("/cancel_order", methods=['POST'])
def cancel_order():
    '''
        Taking in trackingID from UI
    '''
    # Invoke ACTIVITY microservice to
    # 1. Set delivery_desc to "..." -> shipper input in UI
    # 2. Set delivery_status to "Canceled" -> automatic input from UI
    # 3. Sent to activity_log

    # invoke SHIPPER microservice to get shipperId and shipperEmail to inform them of the canceled order.
    # Use AMQP to invoke SEND_SMS microservice after retrieving receiverPhone from ORDER microservice.
    # Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice.
    if request.is_json:
        try:
            trackingID = request.get_json()
            print("\nReceived a tracking_id to be canceled in JSON:", str(trackingID))

            result = processCancelOrder(trackingID)
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
                "message": "cancel_order.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processCancelOrder(trackingID):
    # 1. Get trackingID from order microservice
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    tracking_URL = order_URL + '/tracking/' + str(trackingID["trackingID"])
    order_result = invoke_http(tracking_URL, method='GET', json=None)
    print('order_result:', order_result)

    # 2. Display canceled order in activity log
    # Create the activity log for canceled order
    code = order_result["code"]

    if code in range(200, 300):
        # Invoke the activity microservice
        print('\n-----Invoking activity microservice-----')
        # order_result = json.dumps(order)
        message = {
            "code": 200,
            "data": {
                "tracking_id": trackingID['trackingID'],
                "delivery_status": "Cancelled",
                "delivery_desc": "Order has been canceled by shipper."
            }
        }
        msg = json.dumps(message)
        amqp_setup.check_setup()
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="cancel.order",
                                         body=msg, properties=pika.BasicProperties(delivery_mode=2))
        print("\nCanceled status published to the RabbitMQ Exchange:", msg)
    else:
        print('\nFailed to cancel order in activity')

    # 3. Retrieve shipper Email and ID
    if code in range(200, 300):
        info = order_result["data"]
        shipperID = info["shipperID"]
        retrieve_ShipperURL = shipper_URL + '/' + str(shipperID)
        shipper_result = invoke_http(
            retrieve_ShipperURL, method="GET", json=None)
        shipper = shipper_result["data"]
        print("\n========shipper result data is: =======\n",
              shipper_result['data'])
        shipper_email = shipper["shipperEmail"]
        # if error is thrown, append to error_msg
    else:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while retrieving shipper email. "
            }
        ), 500

    # 4. Email shipper
    email_content = "This is to inform you that Tracking ID: " + \
        str(trackingID["trackingID"]) + " has been canceled."
    email_msg = {
        "toEmail": shipper_email,
        "subject": "Order has been canceled",
        "content": email_content
    }
    email_message = json.dumps(email_msg)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="canceled.email",
                                     body=email_message)

    # 5. Inform receiver
    recipient = info["receiverPhone"]
    msg = "[CAMELCOURIER] Your order " + \
        str(trackingID["trackingID"]) + " has been canceled."
    sms_msg = {
        "toPhone": recipient,
        "content": msg
    }
    sms_message = json.dumps(sms_msg)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="canceled.sms",
                                     body=sms_message)

    # 6. Return order as a json object with codes
    return order_result


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for canceling an order...")
    app.run(host="0.0.0.0", port=5009, debug=True)
