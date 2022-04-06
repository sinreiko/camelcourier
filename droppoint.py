# imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root:root@localhost:3306/camelDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)
CORS(app)

# database setup


class Droppoint(db.Model):
    __tablename__ = 'droppoint'

    placeID = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __init__(self, address, placeID):
        self.address = address
        self.placeID = placeID

    def json(self):
        return {"address": self.address, "placeID": self.placeID}


# return all droppoints function
@app.route("/droppoint")
def get_all():
    droppoints = Droppoint.query.all()
    if len(droppoints):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "droppoints": [droppoint.json() for droppoint in droppoints]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no droppoints."
        }
    ), 404


# return droppoints corresponding to given region
@app.route("/droppoint/<string:region>")
def find_by_region(region):
    droppoints = Droppoint.query.filter_by(region=region)
    if droppoints:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "droppoints": [droppoint.json() for droppoint in droppoints]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no droppoints in this region."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)
