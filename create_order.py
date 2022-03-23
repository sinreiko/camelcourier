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
from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)

# [TO REPLACE] URLs to call
book_URL = "http://localhost:5000/book"
order_URL = "http://localhost:5001/order"
shipping_record_URL = "http://localhost:5002/shipping_record"
activity_log_URL = "http://localhost:5003/activity_log"
error_URL = "http://localhost:5004/error"


@app.route("/create_order", methods=['POST'])
def place_order():
    '''
        Takes in POST inputs for
            - shipperID
            - receiverName
            - receiverAddress
            - receiverPhone
            - receiverEmail
        and runs the procedure above (line 13-18)
    '''
    # Check input format and data of the request are JSON

    try:
        shipperID = request.args.get("shipperID")
        receiverName = request.args.get("receiverName")
        receiverAddress = request.args.get("receiverAddress")
        receiverPhone = request.args.get("receiverPhone")
        receiverEmail = request.args.get("receiverEmail")
        print("\nReceived an order in JSON:", order)
        result = processCreateOrder(shipperID,receiverName,receiverAddress, receiverPhone,receiverEmail)
        return jsonify(result), result["code"]

    except Exception as e:
        # Unexpected error in code
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
        print(ex_str)

        return jsonify({
            "code": 500,
            "message": "place_order.py internal error: " + ex_str
        }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processCreateOrder(shipperID,receiverName,receiverAddress, receiverPhone,receiverEmail):
    # 1. create an error message log
    err_msg = ""
    # 2. Send the order info (all params) into order microservice
    # Invoke the order microservice

        # if error is thrown, append to err_msg

    # 3. Create order in activity log
        # create the activity log

    # 4. Retrieve shipper Email

        # if error is thrown, append to err_msg

    # 5. Email shipper

    # 6. Inform receiver

    # 7. Return created order as a json object with codes
    return {}


# Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for creating an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
