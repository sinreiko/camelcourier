from twilio.rest import Client
from flask import Flask

import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/update")
def sendClientUpdate():
    # Your Account SID from twilio.com/console
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    # Your Auth Token from twilio.com/console
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+6593877839",
        from_="+15405965349",
        body="Hello from Python!")
    return message.sid


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5566, debug=True)
