# imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# NOTE! main db name changed to camelcourier. Pls import the new sql called camelcourier!

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/camelcourier'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# database setup
class Droppoint(db.Model):
    __tablename__ = 'droppoint'

    longitude = db.Column(db.Float, primary_key=True)
    latitude = db.Column(db.Float, primary_key=True)
    region = db.Column(db.String(100), nullable=False)

    def __init__(self, longitude, latitude, region):
        self.longitude = longitude
        self.latitude = latitude
        self.region = region

    def json(self):
        return {"longitude": self.longitude, "latitude": self.latitude, "region": self.region}


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
    app.run(host='0.0.0.0', port=5000, debug=True)
