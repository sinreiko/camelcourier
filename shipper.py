import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
from os import environ

app = Flask(__name__)
# NOTE! main db name changed to camelcourier. Pls import the new sql called camelcourier!
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://is213@localhost:3306/camelDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

CORS(app)


class Shipper(db.Model):
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
        return {"shipperName": self.shipperID,
                "shipperName": self.shipperName,
                "shipperAddress": self.shipperAddress,
                "shipperPhone": self.shipperPhone,
                "shipperEmail": self.shipperEmail,
                "createdDate": self.createdDate,
                "modifiedDate": self.modifiedDate}


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

# try to implement facebook unrestful api for shipper account sign in


@app.route("/shipper/<string:shipperID>", methods=['POST'])
def create_shipper(shipperID):
    if (Shipper.query.filter_by(shipperID=shipperID).first()):
        return jsonify(
            {
                "code": 400,
                "data": {
                    "shipperID": shipperID
                },
                "message": "Shipper already exists in the database."
            }
        ), 400

    data = request.get_json()
    shipper = Shipper(shipperID, **data)

    try:
        db.session.add(shipper)
        db.session.commit()
    except:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "shipperID": shipperID
                },
                "message": "An error occurred creating the shipper account entry."
            }
        ), 500

    return jsonify(
        {
            "code": 201,
            "data": shipper.json()
        }
    ), 201


if __name__ == '__main__':
    print("This is flask for " +
          os.path.basename(__file__) + ": manage shippers ...")
    app.run(host='0.0.0.0', port=5002, debug=True)
