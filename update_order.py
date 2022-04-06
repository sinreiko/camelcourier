from email import message
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
order_URL = environ.get('order_URL') or "http://localhost:5000/order"
# activity_URL = environ.get('activity_URL') or "http://activity:5001/activity"
shipper_URL = environ.get('shipper_URL') or "http://localhost:5002/shipper"


@app.route("/update_order/update/<string:status>", methods=['POST'])
def update_order(status):
    '''
    Taking in tracking ID from UI
    '''
    # Invoke ACTIVITY microservice to
    # 1. Set delivery_desc to "..." -> driver input in UI
    # 2. Set delivery_status to "Accepted/Delayed/Completed" -> automatic input from UI
    # 3. Sent to activity_log

    # invoke SHIPPER microservice to get shipperId and shipperEmail
    # Use AMQP to invoke SEND_SMS microservice after retrieving receiverPhone from ORDER microservice.
    # Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice
    if request.is_json:
        try:
            order = request.get_json()
            print("\nAccepted an order in JSON:", order)

            # 1. Send order info
            result = updateOrder(status, order)
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


def updateOrder(status, order):
    # 1. Get tracking id from order microservice
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    tracking_URL = order_URL + '/tracking/' + str(order["trackingID"])
    order_result = invoke_http(tracking_URL, method='GET', json=None)
    print('order_result:', order_result)

    code = order_result["code"]

    ######## Pick up Order #########
    if status == 'pickup':
        if code in range(200, 300):
            # Invoke the activity microservice
            print('\n-----Invoking activity microservice-----')
            # order_result = json.dumps(order)
            order_message = {
                "code": 200,
                "data": {
                    "tracking_id": order['trackingID'],
                    "delivery_status": "Pickup",
                    "delivery_desc": "Order has been picked up by driver."
                }
            }
            msg = json.dumps(order_message)
            amqp_setup.check_setup()
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="accept.order",
                                             body=msg, properties=pika.BasicProperties(delivery_mode=2))
            print("\nAccept status published to the RabbitMQ Exchange:", msg)

        else:
            print('\nFailed to create accepted order in activity')

        # 4. Retrieve shipper Email and ID
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
            # if error is thrown, append to err_msg
        else:
            return jsonify(
                {
                    "code": 500,
                    "data": {
                        "email": shipper_email
                    },
                    "message": "An error occurred while retrieving shipper email. "
                }
            ), 500

        # 5. Email shipper
        email_content = "This is to inform you that Tracking ID: " + \
            str(order["trackingID"]) + " has been picked up"

        email_msg = {
            "toEmail": shipper_email,
            "subject": "Order has been accepted",
            "content": email_content
        }

        email_message = json.dumps(email_msg)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="accept.email",
                                         body=email_message)

        # 6. Inform receiver
        recipient = info["receiverPhone"]
        msg = "[CAMELCOURIER] Your order " + \
            str(order["trackingID"]) + " has been picked up."
        sms_msg = {
            "toPhone": recipient,
            "content": msg
        }
        sms_message = json.dumps(sms_msg)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="accept.sms",
                                         body=sms_message)

        # 6. Return order as a json object with codes
        return order_result

    ######## Delay Order #########
    elif status == 'delay':
        if code in range(200, 300):
            # Invoke the activity microservice
            print('\n-----Invoking activity microservice-----')
            # order_result = json.dumps(order)
            order_message = {
                "code": 200,
                "data": {
                    "tracking_id": order['trackingID'],
                    "delivery_status": "Delayed",
                    "delivery_desc": "Order has been delayed by driver."
                }
            }
            msg = json.dumps(order_message)
            amqp_setup.check_setup()
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="delay.order",
                                             body=msg, properties=pika.BasicProperties(delivery_mode=2))
            print("\nDelay status published to the RabbitMQ Exchange:", msg)

        else:
            print('\nFailed to create delayed order in activity')

        # 4. Retrieve shipper Email and ID
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
            # if error is thrown, append to err_msg
        else:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred while retrieving shipper email. "
                }
            ), 500

        # 5. Email shipper
        email_content = "This is to inform you that Tracking ID: " + \
            str(order["trackingID"]) + " has been delayed"

        email_msg = {
            "toEmail": shipper_email,
            "subject": "Order has been delayed",
            "content": email_content
        }

        email_message = json.dumps(email_msg)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="delayed.email",
                                         body=email_message)

        # 6. Inform receiver
        recipient = info["receiverPhone"]
        msg = "[CAMELCOURIER] Your order " + \
            str(order["trackingID"]) + " has been delayed."
        sms_msg = {
            "toPhone": recipient,
            "content": msg
        }
        sms_message = json.dumps(sms_msg)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="delayed.sms",
                                         body=sms_message)

        # 6. Return order as a json object with codes
        return order_result

    ######## Complete Order #########
    elif status == 'complete':
        if code in range(200, 300):
            # Invoke the activity microservice
            print('\n-----Invoking activity microservice-----')
            # order_result = json.dumps(order)
            order_message = {
                "code": 200,
                "data": {
                    "tracking_id": order['trackingID'],
                    "delivery_status": "Completed",
                    "delivery_desc": "Order has been completed by driver."
                }
            }
            msg = json.dumps(order_message)
            amqp_setup.check_setup()
            amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="complete.order",
                                             body=msg, properties=pika.BasicProperties(delivery_mode=2))
            print("\nCompleted status published to the RabbitMQ Exchange:", msg)

        else:
            print('\nFailed to create completed order in activity')

        # 4. Retrieve shipper Email and ID
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
            # if error is thrown, append to err_msg
        else:
            return jsonify(
                {
                    "code": 500,
                    "message": "An error occurred while retrieving shipper email. "
                }
            ), 500

        # 5. Email shipper
        email_content = "This is to inform you that Tracking ID: " + \
            str(order["trackingID"]) + " has been completed"

        email_msg = {
            "toEmail": shipper_email,
            "subject": "Order is completed",
            "content": email_content
        }

        email_message = json.dumps(email_msg)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="completed.email",
                                         body=email_message)

        # 6. Inform receiver
        recipient = info["receiverPhone"]
        msg = "[CAMELCOURIER] Your order " + \
            str(order["trackingID"]) + " has been completed."
        sms_msg = {
            "toPhone": recipient,
            "content": msg
        }
        sms_message = json.dumps(sms_msg)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="completed.sms",
                                         body=sms_message)

        # 6. Return order as a json object with codes
        return order_result


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for updating order...")
    app.run(host="0.0.0.0", port=5008, debug=True)
