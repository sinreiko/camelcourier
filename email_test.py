# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from flask import Flask, request
import json, requests

app = Flask(__name__)

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
    # recipient=request.json.get('toEmail')
    # subject=request.json.get('subject')
    # msg=request.json.get('content')
    recipient="smlee.2020@smu.edu.sg"
    subject="test email"
    msg="Sending message is fun with Sendgrid!"

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
    app.run(host='0.0.0.0', port=9000, debug=True)

