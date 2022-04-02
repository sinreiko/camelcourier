import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
import json
import amqp_setup

monitorBindingKey = "*.email"


def receiveEmail():
    amqp_setup.check_setup()

    queue_name = "Email"

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    # an implicit loop waiting to receive messages;
    amqp_setup.channel.start_consuming()
    # it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


# required signature for the callback; no return
def callback(channel, method, properties, body):
    print("\nReceived an email by " + __file__)
    sendEmailUpdate(json.loads(body))
    print()


def sendEmailUpdate(request):
    '''
        Takes in JSON object as input with structure
        {
            "toEmail":<email address>,
            "subject":<email subject>,
            "content":<email content>
        }
    '''
    recipient = request['toEmail']
    subject = request['subject']
    msg = request['content']
    # recipient="leeshaoming78@gmail.com"
    # subject="test email"
    # msg="Sending message is fun with Sendgrid!"

    sg = sendgrid.SendGridAPIClient(
        api_key='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')
    # Change to your verified sender
    from_email = Email("camelcourier06@gmail.com")
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
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveEmail()
