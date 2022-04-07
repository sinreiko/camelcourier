# ------------
#                   O v e r v i e w
# This is the complex microservice for valuing an order in the Shipper's UI
# =======================================
# ------    C o m p o n e n t s
# --- rate.py
# --- Google Maps distance matrix API (external service)

# ------    P r o c e d u r e
# 1-- Shipper finds out a cost estimation after setting pickupAddress (either doorstep or drop-off)
# 2-- Request quote {pickupAddress, receiverAddress, size} to valuing.py
# 3-- Find distance between {pickupAddress, receiverAddress} using Google Maps distance matrix API
# 4-- Return distance
# 5-- Request pricing {distance, size} from rate.py
# 6-- Return price to valuing.py
# 7-- Return and display pricing on Shipper's UI
# =======================================

#   Imports
# ------------
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys
from os import environ

import requests
from invokes import invoke_http

app = Flask(__name__)
CORS(app)


@app.route("/valuing", methods=['POST'])
def request_price():
    '''
        Takes in POST inputs for json object with the following:
            - pickupAddress
            - receiverAddress
            - size
        and runs the procedure above (line 10-16)
    '''
    # Check input format and data of the request are JSON
    if request.is_json:
        try:
            # 2-- Request quote {trackingID, size} to valuing.py
            size_info = request.get_json()
            print("\nValuing a price estimation in JSON:", size_info)
            result = processValuing(size_info)

            # 7-- Return and display pricing on Shipper's UI
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
                "message": "valuing.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400


def processValuing(size_info):
    '''
        size_info is a json with:
            pickupAddress
            receiverAddress
            size
    '''
    # print('\n-----Invoking order microservice-----')
    # order_URL = environ.get('order_URL') or "http://localhost:5000/order"
    # order_URL += "/tracking/" + str(size_info['trackingID'])
    # order_result = invoke_http(order_URL, method='GET', json=None)
    # print('order_result:', order_result)

    # code=order_result["code"]
    # info=order_result['data']
    #   UPDATE: front end already has the addresses, so there's no longer a need to call order

    pickupAddress = size_info['pickupAddress']
    receiverAddress = size_info['receiverAddress']

    # 3-- Find distance between {pickupAddress, receiverAddress} using Google Maps distance matrix API
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + pickupAddress + \
        "&destinations=" + receiverAddress + \
        "&key=AIzaSyCtH98HlunuSLPLGvBf0HmEPnPd6YIye5M"
    output = requests.get(url).json()
    print(output)
    
    # 4-- Return distance
    status = output['rows'][0]['elements'][0]['status']
    if status == "ZERO_RESULTS":
        return jsonify({
            "code": 404,
            "message": "The addresses are invalid."
        })
    distance = output['rows'][0]['elements'][0]['distance']['value'] / 1000

    # 5-- Request pricing {distance, size} from rate.py
    rate_URL = environ.get('rate_URL') or "http://localhost:5003/rate"
    rate_URL += "/" + str(distance) + "/" + size_info['size']
    print(rate_URL)
    rate_result = invoke_http(rate_URL, method='GET', json=None)
    print('rate_result:', rate_result)
    # 6-- Return price to valuing.py
    return rate_result


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for valuing an order...")
    app.run(host="0.0.0.0", port=5005, debug=True)
