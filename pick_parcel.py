# ------------
#                   O v e r v i e w
# This is the complex microservice for shipper to select a drop off point for his/her parcel in the Shipper's UI
# =======================================
# ------    C o m p o n e n t s
# --- droppoint.py
# --- order.py
# --- shipper.py
# --- email_test.py
# --- activity.py

# ------    P r o c e d u r e
# 1-- The microservice receives a dropoff point selected for the parcel with shipperID, trackingID, pickupAddress
# 2-- The microservice then updates the order with the given trackingID with the pickupAddress.
# 3-- Shipper's email is obtained through the Shipper microservice
# 4-- Shipper is emailed via Email microservice - AMQP -> sendgrid
# 5-- Activity microservice is called to insert activity of pickup
# =======================================

#   Imports
# ------------
import json
import pika
import amqp_setup
from invokes import invoke_http
import requests
import sys
import os
from os import environ
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

order_URL = environ.get('order_URL') or "http://localhost:5000/order"
# activity_URL = "http://localhost:5001/activity"
shipper_URL = environ.get('shipper_URL') or "http://localhost:5002/shipper"
# droppoint_URL = "http://localhost:5004/droppoint"
# email_URL = "http://localhost:9000/email"


@app.route("/pick_parcel", methods=['POST'])
def pickup():
    if request.is_json:
        try:
            pickup_details = request.get_json()
            print("\nReceived an order in JSON:", pickup_details)

            result = processPickup(pickup_details)
            print('\n------------------------')
            print('\nresult: ', result)
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
                "message": "pick_parcel.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processPickup(pickup_details):
    # 1-- The microservice receives a dropoff point selected for the parcel with shipperID, trackingID, pickupAddress
    # 2-- The microservice then updates the order with the given trackingID with the pickupAddress.

    tracking_id = pickup_details["trackingID"]

    print('\n-----Invoking order microservice-----')
    order_result = invoke_http(
        order_URL + "/" + str(tracking_id), method='PUT', json=pickup_details)
    print('order_result:', order_result)

    code = order_result["code"]
    messsage = json.dumps(order_result)

    if code not in range(200, 300):
        # err handling
        print('\n\n----- Failed to update order with pickupAddress')
        print("\n Returned error 500 code")
        return {
            "code": 500,
            "data": {
                "order_result": order_result
            },
            "message": "Order update has failed and was not updated."
        }
    else:
        # no error
        print('\n\n----- Succcess in updating order with pickupAddress')

    # 3-- Shipper's email is obtained through the Shipper microservice
    shipper_result = invoke_http(
        shipper_URL + "/" + str(pickup_details["shipperID"]), method='GET')
    print('shipper_result:', shipper_result)
    code = shipper_result["code"]

    if code not in range(200, 300):
        # err handling
        print('\n\n----- Failed to get shipper details')
        print("\n Returned error 500 code")
        return {
            "code": 500,
            "data": {
                "order_result": order_result
            },
            "message": "Unable to get shipper details and unable to notify shipper via email."
        }
    else:
        # no error
        print('\n\n----- Success in getting shipper details')
        shipper_email = shipper_result["data"]["shipperEmail"]
        email_content = f"This is to inform you about your order with Tracking ID: {tracking_id} has been successfully updated with the parcel pick up address."
    # 4-- Shipper is emailed via Email microservice -AMQP-> sendgrid
    print('\n\n-----Publishing to the email with routing_key=email-----')
    message = json.dumps({
        "toEmail": shipper_email,
        "subject": "New order has been updated with pick up address",
        "content": email_content
    })

    print("\n==== Publishing to email with routing_key=email =====\n", message)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="email",
                                     body=message, properties=pika.BasicProperties(delivery_mode=2))
    print("\n----- End of publishing to email ------")

    # 5-- Activity microservice is called to insert activity of pickup

    print("\n==== Publishing to activity with routing_key=order =====\n", message)
    message = json.dumps({
        "code": 201,
        "data": {
            "tracking_id": tracking_id,
            "delivery_status": "Waiting for pickup",
            "delivery_desc": "Pick up location has been updated, awaiting for parcel pickup."
        }
    })
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order",
                                     body=message, properties=pika.BasicProperties(delivery_mode=2))
    print("\n----- End of publishing to activity ------")

    return {
        "code": 201,
        "data": {
            "order_result": order_result,
            "shipper_result": shipper_result
        }
    }


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for pick parcel...")
    app.run(host="0.0.0.0", port=5006, debug=True)
