import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
import json
from os import environ

# import cloud database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

app = Flask(__name__)


cred = credentials.Certificate(
    "./esd-camelcourier-firebase-adminsdk-7rkrr-3e74a27669.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://esd-camelcourier-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

CORS(app)


class User(db):
    ref = db.reference("/user")
    name = db.reference("/user/name")
    email = db.reference("/user/email")
    password = db.reference("/user/password")
    type = db.reference("/user/type")

    def __init__(self, name, email, password, type):
        self.name = name
        self.email = email
        self.password = password
        self.type = type

    def json(self):
        return {"name": self.name,
                "email": self.email,
                "password": self.password,
                "type": self.type
                }


@app.route("/user")
def get_all():
    userList = User.query.all()
    if len(userList):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "user": [user.json() for user in userList]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no shippers to be found."
        }
    ), 404


if __name__ == '__main__':
    print("This is flask for " +
          os.path.basename(__file__) + ": get users ...")
    app.run(host='0.0.0.0', port=5000, debug=True)
