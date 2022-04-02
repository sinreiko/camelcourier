#!/usr/bin/env python3
# activity log service

# for database
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


from datetime import datetime
from os import environ
import json
import os

# for amqp
import amqp_setup

#### Linking to DB ####
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
                          default=datetime.now, onupdate=datetime.now)
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


#### Receiving Activity Log ####
monitorBindingKey = "#.order.#"


def receiveActivity():
    amqp_setup.check_setup()

    queue_name = "Activity"

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    # an implicit loop waiting to receive messages;
    amqp_setup.channel.start_consuming()
    # it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


# required signature for the callback; no return
def callback(channel, method, properties, body):
    print("\nReceived an activity log by " + __file__)
    processActivity(json.loads(body))
    print()  # print a new line feed


def processActivity(activity):
    print("Recording an order log:")
    print(activity)
    data = activity["data"]

    # Creating new row in db
    if activity['code'] in range(200,300):
        activityr = Activity(trackingID=data['tracking_id'],
                             deliveryStatus=data['delivery_status'],
                             deliveryDesc=data['delivery_desc'])
    try:
        db.session.add(activityr)
        db.session.commit()
    except Exception as e:
        print("Error encountered: ", e)
        print()

if __name__ == '__main__':
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveActivity()
