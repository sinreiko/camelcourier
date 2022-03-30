#!/usr/bin/env python3
# activity log http service

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from datetime import datetime
from os import environ
import json
import os

#### Getting Activity Log ####
# NOTE! main db name changed to camelcourier. Pls import the new sql called camelcourier!
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root@localhost:3306/camelDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


class Activity(db.Model):
    __tablename__ = 'activity'

    activityID = db.Column(db.Integer, primary_key=True)
    trackingID = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False,
                          default=datetime.now,        onupdate=datetime.now)
    deliveryStatus = db.Column(db.String(30), nullable=False)
    deliveryDesc = db.Column(db.String(130), nullable=False)

    def json(self):
        dto = {
            'activity_id': self.activityID,
            'tracking_id': self.trackingID,
            'timestamp': self.timestamp,
            'delivery_status': self.deliveryStatus,
            'delivery_desc': self.deliveryDesc
        }

        return dto


@app.route("/activity/<string:trackingID>")
def find_activity_by_tracking(trackingID):
    activityList = Activity.query.filter_by(trackingID=trackingID)
    if activityList.count():
        return jsonify(
            {
                "code": 200,
                "data": [activity.json() for activity in activityList]
            }
        )

    return jsonify(
        {
            "code": 404,
            "data": {
                "tracking_id": trackingID
            },
            "message": "No Activity Found."
        }
    ), 404


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": log activities ...")
    app.run(host='0.0.0.0', port=5001, debug=True)
