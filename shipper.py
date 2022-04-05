# ===========================================

#           I M P O R T S

# ----------------
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import json
from os import environ

# ===========================================

#           D B   S E T   U P   A  N D   C U S T O M  C L A S S

# ----------------
app = Flask(__name__)
# NOTE! main db name changed to camelcourier. Pls import the new sql called camelcourier!
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://is213@localhost:3306/camelDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Define a custom class for each shipper record.


class Shipper(db.Model):
    '''
        Takes in the following attributes:
        - shipperID -> autoincrement string to serve as the primary key of the shipper in the db
        - shipperName -> created when shipper inputs name during account sign up
        - shipperAddress -> created when shipper inputs address during account sign up
        - shipperPhone -> created when shipper inputs phone number during account sign up
        - shipperEmail -> created when shipper inputs email during account sign up
        - createdDate -> generated when shipper creates account
        - modifiedDate -> generated when shipper modifies account
    '''
    __tablename__ = 'shipper'
    shipperID = db.Column(db.Integer, primary_key=True)
    shipperName = db.Column(db.String(32), nullable=False)
    shipperAddress = db.Column(db.String(64), nullable=False)
    shipperPhone = db.Column(db.Integer, nullable=False)
    shipperEmail = db.Column(db.String(64), nullable=False)
    createdDate = db.Column(db.DateTime, nullable=False, default=datetime.now)
    modifiedDate = db.Column(db.DateTime, nullable=False,
                             default=datetime.now, onupdate=datetime.now)

    def __init__(self, shipperID, shipperName, shipperAddress, shipperPhone, shipperEmail, createdDate, modifiedDate):
        self.shipperID = shipperID
        self.shipperName = shipperName
        self.shipperAddress = shipperAddress
        self.shipperPhone = shipperPhone
        self.shipperEmail = shipperEmail
        self.createdDate = createdDate
        self.modifiedDate = modifiedDate

    def json(self):
        return {"shipperID": self.shipperID,
                "shipperName": self.shipperName,
                "shipperAddress": self.shipperAddress,
                "shipperPhone": self.shipperPhone,
                "shipperEmail": self.shipperEmail,
                "createdDate": self.createdDate,
                "modifiedDate": self.modifiedDate}

# ===========================================

#           U T I L I T Y   F U N C T I O N S
    # ---------
        # get_all(): Retrieves all entries from the db and returns them in JSON format
    # ---------

# ----------------------------------

    # ---------------[START: get_all]-------------------
    # [TESTED] This url returns all shipper database info in json format
    # This is used to troubleshoot and see if the data in db is ok
    # Uncomment line below to test this function


@app.route("/shipper")
def get_all():
    shipperList = Shipper.query.all()
    if len(shipperList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "shippers": [shipper.json() for shipper in shipperList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no shippers to be found."
        }
    ), 404

    # ----------------[END: get_all]------------------

# ===========================================

#           A P I   F U N C T I O N S
    # -----------
    # find_by_shipperID(): fulfills app route /shipper/<shipperID> to return information of a given shipper ID with method GET
    # -----------

# ----------------------------------

    # -----------------[START: find_by_shipperID]-------------------
# [TESTED] This url fulfills shipper checking.


@app.route("/shipper/<string:shipperID>")
def find_by_shipperID(shipperID):
    shipper = Shipper.query.filter_by(shipperID=shipperID).first()
    if shipper:
        return jsonify(
            {
                "code": 200,
                "data": shipper.json()
            }
        )
    return jsonify(
        {
            "code": 404,
            "data": {
                "shipperID": shipperID
            },
            "message": "Shipper was not found."
        }
    ), 404

    # ---------------[END: find_by_shipperID]-------------------

# ===========================================


# Alternative app call failsafe
if __name__ == '__main__':
    print("This is flask for " +
          os.path.basename(__file__) + ": manage shippers ...")
    app.run(host='0.0.0.0', port=5002, debug=True)
