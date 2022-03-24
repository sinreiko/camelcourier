from crypt import methods
from twilio.rest import Client
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/update", methods=['POST'])
def sendClientUpdate():
    '''
        Takes in JSON object as input with structure
        {
            "toPhone":<phone number>,
            "content":<sms content>
        }
    '''
    # Your Account SID from twilio.com/console
    account_sid = "AC872941965f08ba52b89f8698deae23ab"
    # Your Auth Token from twilio.com/console
    auth_token = "33a25826b94a13ea6c340e92e1ad503b"

    client = Client(account_sid, auth_token)
    
    # recipient=request.json.get('toPhone')
    # msg=request.json.get('content')
    recipient="+6592340039"
    msg="Hello from Python!"
    message = client.messages.create(
        # to="+6593877839",
        to=recipient,
        from_="+15405965349",
        body=msg)
    return message.sid


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5566', debug=True)
