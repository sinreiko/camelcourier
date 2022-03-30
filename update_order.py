from flask import Flask, request, jsonify
from flask_cors import CORS

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
# #book_URL = "http://localhost:5000/book"
# order_URL = environ.get('order_URL') or "http://localhost:5001/order"
# shipping_record_URL = environ.get('shipping_record_URL') or "http://localhost:5002/shipping_record"
# order_URL = environ.get('order_URL') or "http://localhost:5000/order"
# shipper_URL = environ.get('shipper_URL') "http://localhost:5001/shipper"


@app.route("/delay", methods=['PUT'])
def delay():
    # UI automatically sends JSON that contains shipperID, trackingID
    # {
    #    "shipper_id": "S000000000001",
    #    "tracking_id": "FDKS09284023"
    # }

    # Invoke ACTIVITY microservice to
    # 1. Retrieve trackingID from ORDER microservice
    # 2. Set delivery_desc to "..." -> driver input in UI
    # 3. Set delivery_status to "Delayed" -> automatic input from UI
    # 4. Sent to activity_log

    # invoke SHIPPER microservice after getting shipperId and shipperEmail
    # Use AMQP to invoke SEND_SMS microservice after retrieving receiverPhone from ORDER microservice.
    # Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice\
    if request.is_json:
        try:
            order = request.get_json()
            print("\nDelayed an order in JSON:", order)

            # 1. Send order info
            result = delayOrder(order)
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
                "message": "update_order.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def delayOrder(order):
    # 1. Send the order info (all params) into order microservice
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    order_result = invoke_http(order_URL, method='POST', json=order)
    print('order_result:', order_result)

    code = order_result["code"]
    info_json = order_result['data']
    info = json.loads(info_json)

    # Invoke the activity microservice
    print('\n-----Invoking activity microservice-----')
    # order_result = json.dumps(order)
    message = {
        "code": 200,
        "data": {
            "tracking_id": order['tracking_id'],
            "delivery_status": "Delayed",
            "delivery_desc": "Order has been delayed by driver."
        }
    }
    print(message)
    amqp_setup.check_setup()
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="delay.order",
                                     body=json.dumps(message), properties=pika.BasicProperties(delivery_mode=2))
    print("\nDelay status published to the RabbitMQ Exchange:", message)
    return {
        "code": 201,
        "data": {"delay_data": message},
        "message": "Order delay sent to activity log."
    }

    shipperID = info.shipperID
    shipper_URL += '/'+shipperID
    email_result = invoke_http(shipper_URL, method="GET", json=None)
    if code in range(200, 300):
        info_email_json = email_result["data"]
        info_email = json.loads(info_email_json)
        shipper_email = info_email.shipperEmail
        # if error is thrown, append to err_msg
    else:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "email": email_result
                },
                "message": "An error occurred while retrieving shipper email. "
            }
        ), 500

    # 5. Email shipper
    email_content = "This is to inform you that Tracking ID: " + \
        tracking_id+" has been delayed"

    message = jsonify(
        {
            "toEmail": shipper_email,
            "subject": "Order has been delayed",
            "msg": email_content
        }
    )

    # Replace with this after AMQP has been set up

    # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="new.email",
    #         body=message)

    # 5. Inform receiver
    recipient = info.receiverPhone
    msg = "[Camel Couriers] Your order "+tracking_id+" has been delayed."
    sms_message = jsonify(
        {
            "toPhone": recipient,
            "content": msg
        }
    )
    sms_status = invoke_http(sms_URL, method="POST", json=sms_message)
    print(sms_status)

    # 6. Return cancled order as a json object with codes
    return order_result


@app.route("/complete", methods=['PUT'])
def complete():
    # invoke ORDER microservice to get its shipperID, trackingID
    # invoke ACTIVITY microservice to
    # Retrieve trackingID from ORDER microservice
    # Set delivery_desc to "..." -> driver input in UI
    # Set delivery_status to "Complete" -> automatic input from UI
    # invoke SHIPPER microservice after getting shipperId and get shipperEmail
    # Use AMQP to invoke SEND_SMS microservice after retrieving receiverPhone from ORDER microservice.
    # Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice
    if request.is_json:
        try:
            order = request.get_json()
            print("\nCompleted an order in JSON:", order)

            # 1. Send order info
            result = completeOrder(order)
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
                "message": "update_order.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def completeOrder(order):
    # 1. Send the order info (all params) into order microservice
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    order_result = invoke_http(order_URL, method='POST', json=order)
    print('order_result:', order_result)

    code = order_result["code"]
    info_json = order_result['data']
    info = json.loads(info_json)

    # Invoke the activity microservice
    print('\n-----Invoking activity microservice-----')
    # order_result = json.dumps(order)
    message = {
        "code": 200,
        "data": {
            "tracking_id": order['tracking_id'],
            "delivery_status": "Completed",
            "delivery_desc": "Order has been completed by driver."
        }
    }
    print(message)
    amqp_setup.check_setup()
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="complete.order",
                                     body=json.dumps(message), properties=pika.BasicProperties(delivery_mode=2))
    print("\nComplete status published to the RabbitMQ Exchange:", message)
    return {
        "code": 201,
        "data": {"complete_data": message},
        "message": "Order complete sent to activity log."
    }

    shipperID = info.shipperID
    shipper_URL += '/'+shipperID
    email_result = invoke_http(shipper_URL, method="GET", json=None)
    if code in range(200, 300):
        info_email_json = email_result["data"]
        info_email = json.loads(info_email_json)
        shipper_email = info_email.shipperEmail
        # if error is thrown, append to err_msg
    else:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "email": email_result
                },
                "message": "An error occurred while retrieving shipper email. "
            }
        ), 500

    # 5. Email shipper
    email_content = "This is to inform you that Tracking ID: " + \
        tracking_id + " has been completed"

    message = jsonify(
        {
            "toEmail": shipper_email,
            "subject": "Order has been completed",
            "msg": email_content
        }
    )

    # Replace with this after AMQP has been set up

    # amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="new.email",
    #         body=message)

    # 5. Inform receiver
    recipient = info.receiverPhone
    msg = "[Camel Couriers] Your order " + tracking_id + " has been completed."
    sms_message = jsonify(
        {
            "toPhone": recipient,
            "content": msg
        }
    )
    sms_status = invoke_http(sms_URL, method="POST", json=sms_message)
    print(sms_status)

    # 6. Return cancled order as a json object with codes
    return order_result


@app.route("/accept", methods=['PUT'])
def accept():
    # Invoke ORDER microservice to get tracking ID
    # Invoke ACTIVITY microservice to create a new activity log
    # Set delivery_desc to "on the way to pick up" -> driver input in UI
    # Set delivery_status to "Awaiting Pick Up" -> driver input in UI
    # Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice
    # Simple check of input format and data of the request are JSON
    return


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for updating order...")
    app.run(host="0.0.0.0", port=5009, debug=True)
