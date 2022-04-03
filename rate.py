# imports
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from os import environ

app = Flask(__name__)
# NOTE! main db name changed to camelcourier. Pls import the new sql called camelcourier!

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'dbURL') or 'mysql+mysqlconnector://root@localhost:3306/camelDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# database setup
class Rate(db.Model):
    __tablename__ = 'rate'

    size = db.Column(db.String(64), primary_key=True, nullable=False)
    priceperkm = db.Column(db.Float, nullable=False)

    def __init__(self, size, priceperkm):
        self.size = size
        self.priceperkm = priceperkm

    def json(self):
        return {"size": self.size, "priceperkm": self.priceperkm}


# return price corresponding to given distance and size
@app.route("/rate/<string:distance>/<string:size>")
def calculate_price(distance, size):
    rates = Rate.query.filter_by(size=size)
    if rates:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "price": round(rates[0].priceperkm * float(distance),2)
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "Size given does not exist."
        }
    ), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
