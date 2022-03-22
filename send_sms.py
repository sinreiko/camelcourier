from twilio.rest import Client
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/update")
def sendClientUpdate():
    # Your Account SID from twilio.com/console
    account_sid = "AC872941965f08ba52b89f8698deae23ab"
    # Your Auth Token from twilio.com/console
    auth_token = "33a25826b94a13ea6c340e92e1ad503b"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        # to="+6593877839",
        to="+6592340039",
        from_="+15405965349",
        body="Hello from Python!")
    return message.sid


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5566' debug=True)
