from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

#URL of all the simple microservices that you're contacting
# #book_URL = "http://localhost:5000/book"
# order_URL = environ.get('order_URL') or "http://localhost:5001/order" 
# shipping_record_URL = environ.get('shipping_record_URL') or "http://localhost:5002/shipping_record" 

@app.route("/accept", methods=['PUT'])
def accept():
    #Invoke ORDER microservice /order/accept
    #Invoke ACTIVITY microservice to create a new activity log
        # Retrieve tracking ID from ORDER microservice
        # Set delivery_desc to "on the way to pick up" -> driver input in UI
        # Set delivery_status to "Awaiting Pick Up" -> driver input in UI
    #Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice
    return

@app.route("/delay", methods=['PUT'])
def delay():
    #invoke ORDER microservice to get its shipperID, trackingID
    #invoke ACTIVITY microservice to 
        # Retrieve trackingID from ORDER microservice
        # Set delivery_desc to "..." -> driver input in UI 
        # Set delivery_status to "Delayed" -> automatic input from UI
    #invoke SHIPPER microservice after getting shipperId and get shipperEmail
    #Use AMQP to invoke SEND_SMS microservice after retrieving receiverPhone from ORDER microservice.
    #Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice
    return

@app.route("/complete", methods=['PUT'])
def complete():
    #invoke ORDER microservice to get its shipperID, trackingID
    #invoke ACTIVITY microservice to 
        # Retrieve trackingID from ORDER microservice
        # Set delivery_desc to "..." -> driver input in UI 
        # Set delivery_status to "Complete" -> automatic input from UI
    #invoke SHIPPER microservice after getting shipperId and get shipperEmail
    #Use AMQP to invoke SEND_SMS microservice after retrieving receiverPhone from ORDER microservice.
    #Use AMQP to invoke EMAIL microservice after retrieving shipper's email from SHIPPER microservice
    return