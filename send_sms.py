import amqp_setup
from twilio.rest import Client
from flask import Flask, request, jsonify 
import json, requests

app = Flask(__name__)

#### Receiving Activity Log ####
monitorBindingKey = "#.sms"

def receiveActivity():
    amqp_setup.check_setup()

    queue_name = "SMS"
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

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
    auth_token = "b01281d78fe392ab1130cb00745eeef9"

    client = Client(account_sid, auth_token)
    
    recipient=request.json.get('toPhone')
    msg=request.json.get('content')
    #recipient="+6592340039"
    #msg="Hello from Python!"
    message = client.messages.create(
        # to="+6593877839",
        to=recipient,
        from_="+15405965349",
        body=msg)
    return message.sid


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5566', debug=True)
