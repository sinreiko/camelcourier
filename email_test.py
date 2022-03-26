import amqp_setup
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from flask import Flask, request, jsonify
import json, requests

app = Flask(__name__)

monitorBindingKey = "#.email"

def receiveEmail():
    amqp_setup.check_setup()

    queue_name = "Email"
    
    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an sms by " + __file__)
    sendEmailUpdate()
    print()

@app.route("/email", methods=['POST'])
def sendEmailUpdate():
    '''
        Takes in JSON object as input with structure
        {
            "toEmail":<email address>,
            "subject":<email subject>,
            "content":<email content>
        }
    '''
    recipient=request.json.get('toEmail')
    subject=request.json.get('subject')
    msg=request.json.get('content')
    # recipient="leeshaoming78@gmail.com"
    # subject="test email"
    # msg="Sending message is fun with Sendgrid!"

    sg = sendgrid.SendGridAPIClient(api_key='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')
    from_email = Email("camelcourier06@gmail.com")  # Change to your verified sender
    to_email = To(recipient)  # Change to your recipient
    content = Content("text/plain", msg)
    mail = Mail(from_email, to_email, subject, content)
    
    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    return "Email has been sent"

if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    receiveEmail()

