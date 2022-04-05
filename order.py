# ===========================================

#           I M P O R T S

# ----------------
from lib2to3.pgen2 import driver
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, timedelta
from flask_cors import CORS
import json
import requests
from os import environ

from sqlalchemy import null, func

# ===========================================

#           D B   S E T   U P   A  N D   C U S T O M  C L A S S

# ----------------
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/camelDB'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Define a custom class for each delivery order.


class Order(db.Model):
    '''
        Takes in the following attributes:
        - trackingID -> autoincrement string to serve as the primary key of the order in the db
        - driverID -> created when driver signs up for an account.
        - shipperID -> created when shipper signs up for an account.
        - deliveryStage -> takes in 'to pick up','en route','delivered','returning to sender','returned to sender'
        - deliveryDate -> generated when adding a new order

    '''
    __tablename__ = 'order'

    trackingID = db.Column(db.Integer, primary_key=True, nullable=True)
    driverID = db.Column(db.String(13), nullable=True)
    shipperID = db.Column(db.String(13), nullable=False)
    receiverName = db.Column(db.String(30), nullable=False)
    receiverAddress = db.Column(db.String(100), nullable=False)
    receiverPhone = db.Column(db.String(30), nullable=False)
    receiverEmail = db.Column(db.String(50), nullable=False)
    pickupAddress = db.Column(db.String(100), nullable=True)

    def __init__(self, trackingID, driverID, shipperID, receiverName, receiverAddress, receiverPhone, receiverEmail, pickupAddress):
        self.trackingID = trackingID
        self.driverID = driverID
        self.shipperID = shipperID
        self.receiverName = receiverName
        self.receiverAddress = receiverAddress
        self.receiverPhone = receiverPhone
        self.receiverEmail = receiverEmail
        self.pickupAddress = pickupAddress

    def json(self):
        return {"trackingID": self.trackingID, "driverID": self.driverID, "shipperID": self.shipperID, "receiverName": self.receiverName, "receiverAddress": self.receiverAddress, "receiverPhone": self.receiverPhone, "receiverEmail": self.receiverEmail, "pickupAddress": self.pickupAddress}

# ===========================================

#           U T I L I T Y   F U N C T I O N S
    # ---------
        # get_all(): Retrieves all entries from the db and returns them in JSON format
        # find_driver(): Returns driverID of the first driver with the least amount of orders assigned
    # ---------

# ----------------------------------

    # ---------------[START: get_all]-------------------
    # [TESTED] This url returns all order database info in json format
    # This is used to troubleshoot and see if the data in db is ok
    # Uncomment line below to test this function


@app.route("/order/checkall")
def get_all():
    '''returns a JSON object with list of all order objects 
        [{trackingID, driverID, shipperID, receiverName, receiverAddress, receiverPhone, receiverEmail, pickupAddress},
        {},{}...]
    '''
    # SELECT * from order
    order = Order.query.all()

    if len(order):
        return jsonify(
            {
                "code": 200,
                "data": {
                    'orders': [ord.json() for ord in order]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no orders."
        }
    ), 404
    # ----------------[END: get_all]------------------

    # -----------------[START: find_driver]-------------------
    # [TESTED] Finds the driver with the least orders to assign the new order to
    # Uncomment line below to test this function in Postman


def find_driver():
    ''' returns <string:driverID> with the least orders 
        SQL Equivalent: SELECT count(*),driverID FROM `order` group by driverID ORDER BY count(*)
    '''
    order = Order.query.with_entities(func.count(Order.trackingID), Order.driverID).group_by(
        Order.driverID).order_by(func.count(Order.trackingID)).first()
    if len(order):
        return order.driverID
    return False

    # ---------------[END: find_driver]-------------------

# ===========================================

#           A P I   F U N C T I O N S
    # -----------
    # find_order_by_no(): fulfills app route /order/<trackingID> to return information of a given tracking ID with method GET
    # create_order(): fulfills app route /order to add a new order, generate a trackingID and assign a driver with method POST
    # update_order(): fulfills app route /order/update to update the pickupAddress of an entry given a trackingID with method PUT
    # driver(driverID): returns all orders by a given driver ID
    # -----------

# ----------------------------------

    # -----------------[START: find_order_by_driver]-------------------
# [TESTED] This url fulfills order checking.


@app.route("/order/find/<string:userType>/<string:userID>")
def find_by_driver(userType,userID):
    '''
        returns the order information (trackingID, driverID, shipperID, deliveryStage, deliveryDate) given a trackingID
    '''
    if userType=="driver":
        order = Order.query.filter_by(driverID=userID).all()
    if userType=="shipper":
        order = Order.query.filter_by(shipperID=userID).all()
    if len(order):
        return jsonify(
            {
                "code": 200,
                "data": {
                    'orders': [ord.json() for ord in order]
                }
            }
        )
        
    return jsonify(
        {
            "code": 404,
            "message": "There are no orders."
        }
    ), 404
    # ----------------[END: find_order_by_driver]------------------

    # -----------------[START: find_order_by_driver]-------------------


@app.route("/order/tracking/<string:trackingID>")
def find_by_order_no(trackingID):
    '''
        returns the order information (trackingID, driverID, shipperID, deliveryStage, deliveryDate) given a trackingID
    '''
    order = Order.query.filter_by(trackingID=trackingID).first()
    if order:
        return jsonify(
            {
                "code": 200,
                "data": order.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Order not found."
        }
    ), 404
    # ----------------[END: find_order_by_no]------------------

    # ----------------[START: create_order]------------------
# [TESTED] This URL adds a new order given a shipperID.

# Creates (trackingID: AUTOINC (server end), driverID: FUNC_CALL, shipperID: SESSION_VARIABLE, receiverName: USER_INPUT, receiverAddress: USER_INPUT, receiverPhone: USER_INPUT, receiverEmail: USER_INPUT, pickupAddress: NULL


@app.route("/order", methods=['POST'])
def create_order():
    '''
        This function invokes generate_driver_date() to find the next available date and uses mySQL's autoincrement function to generate a new trackingID.
        returns the created order or error message in JSON format
    '''
    trackingID = None
    shipperID = request.json.get('shipperID')
    driver = find_driver()
    if driver:
        driverID = driver
    else:
        return jsonify(
            {
                "code": 404,
                "message": "We do not have drivers for the next two weeks, try again soon!"
            }
        )
    receiverName = request.json.get('receiverName')
    receiverAddress = request.json.get('receiverAddress')
    receiverPhone = request.json.get('receiverPhone')
    receiverEmail = request.json.get('receiverEmail')
    pickupAddress = request.json.get('pickupAddress')

    # data = request.get_json() <- fallback
    newOrder = Order(trackingID, driverID, shipperID, receiverName,
                     receiverAddress, receiverPhone, receiverEmail, pickupAddress)
    try:
        db.session.add(newOrder)
        status = db.session.commit()
        print(status)
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the order."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": newOrder.json()
        }
    ), 201
    # ----------------[END: create_order]------------------

    # ----------------[START: update_order]------------------
    # [TESTED] This path updates the pickup address of a given order.


@app.route("/order/<string:trackingID>", methods=['PUT'])
def update_order(trackingID):
    '''
        This function finds the order query, changes the pickupAddress and commits to db using ORM to update the row entry
        SQL equivalent: UPDATE order SET pickupAddress = [USER_INPUT] WHERE trackingID = [USER_INPUT]
    '''
    # pickupAddress = request.args.get('pickupAddress')
    # trackingID = request.args.get('trackingID')
    # order = Order.query.filter_by(trackingID=trackingID).first()
    # order.pickupAddress = pickupAddress
# Inquire which type of update the user attempts to make
    info_json = request.json
    if ("driverID" in info_json):
        driverID = info_json.get("driverID")
        order = Order.query.filter_by(trackingID=trackingID).first()
        order.driverID = driverID

    if("pickupAddress" in info_json):
        pickupAddress = info_json.get("pickupAddress")
        order = Order.query.filter_by(trackingID=trackingID).first()
        order.pickupAddress = pickupAddress
    try:
        status = db.session.commit()
        print(status)
    except:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred creating the order."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": order.json()
        }
    ), 201
    # ----------------[END: update_order]------------------

# ===========================================


# Alternative app call failsafe
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
