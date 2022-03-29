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
order_URL = "http://localhost:5000/order"
shipper_URL = "http://localhost:5001/shipper"


@app.route("/delay", methods=['PUT'])
def delay():
    # UI automatically sends JSON that contains shipperID, trackingID
    # {
    #    "shipper_id": "S000000000001",
    #    "tracking_id": "FDKS09284023"
    # }

    # invoke ACTIVITY microservice to
    # Retrieve trackingID from ORDER microservice
    # Set delivery_desc to "..." -> driver input in UI
    # Set delivery_status to "Delayed" -> automatic input from UI
    # invoke SHIPPER microservice after getting shipperId and get shipperEmail
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
    return


@app.route("/accept", methods=['PUT'])
def accept():
    # Invoke ORDER microservice to get tracking ID
    # Invoke ACTIVITY microservice to create a new activity log
    # Set delivery_desc to "on the way to pick up" -> driver input in UI
    # Set delivery_status to "Awaiting Pick Up" -> driver input in UI
    # Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice

    # Simple check of input format and data of the request are JSON
    if request.is_json:
        try:
            order = request.get_json()
            print("\nAccepted an order in JSON:", order)

            # 1. Send order info
            result = acceptOrder(order)
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
                "message": "update.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def acceptOrder(order):
    # Accept the order delivery
    print('\n-----Invoking order microservice-----')
    order_result = invoke_http(orderRetrieve_URL, method='POST', json=order)
    print('order_result:', order_result)

    # Check the order result; if a failure, send it to the error microservice.
    code = order_result["code"]
    if code not in range(200, 300):
        # Inform the error microservice
        print('\n\n-----Invoking error microservice as order fails-----')
        invoke_http(error_URL, method="POST", json=order_result)
        # - reply from the invocation is not used;
        # continue even if this invocation fails
        print("Order status ({:d}) sent to the error microservice:".format(
            code), order_result)

        # 7. Return error
        return {
            "code": 500,
            "data": {"order_result": order_result},
            "message": "Order creation failure sent for error handling."
        }

    # 5. Send new order to shipping
    # Invoke the shipping record microservice
    print('\n\n-----Invoking shipping_record microservice-----')
    shipping_result = invoke_http(
        shipping_record_URL, method="POST", json=order_result['data'])
    print("shipping_result:", shipping_result, '\n')

    # Check the shipping result;
    # if a failure, send it to the error microservice.
    code = shipping_result["code"]
    if code not in range(200, 300):
        # Inform the error microservice
        print('\n\n-----Invoking error microservice as shipping fails-----')
        invoke_http(error_URL, method="POST", json=shipping_result)
        print("Shipping status ({:d}) sent to the error microservice:".format(
            code), shipping_result)

        # 7. Return error
        return {
            "code": 400,
            "data": {
                "order_result": order_result,
                "shipping_result": shipping_result
            },
            "message": "Simulated shipping record error sent for error handling."
        }

    # 7. Return created order, shipping record
    return {
        "code": 201,
        "data": {
            "order_result": order_result,
            "shipping_result": shipping_result
        }
    }


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for updating order...")
    app.run(host="0.0.0.0", port=5008, debug=True)
