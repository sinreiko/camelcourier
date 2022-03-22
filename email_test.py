# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from flask import Flask

app = Flask(__name__)

@app.route("/")
def sendEmailUpdate():
    sg = sendgrid.SendGridAPIClient(api_key='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')
    from_email = Email("camelcourier06@gmail.com")  # Change to your verified sender
    to_email = To("leeshaoming78@gmail.com")  # Change to your recipient
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain", "and easy to do anywhere, even with Python")
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

