from twilio.rest import Client
import json
import requests
import os
import amqp_setup

monitorBindingKey = "*.sms"


def receiveSMS():
    amqp_setup.check_setup()

    queue_name = "SMS"

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    # an implicit loop waiting to receive messages;
    amqp_setup.channel.start_consuming()
    # it doesn't exit by default. Use Ctrl+C in the command window to terminate it.


# required signature for the callback; no return
def callback(channel, method, properties, body):
    print("\nReceived an sms by " + __file__)
    sendClientUpdate(json.loads(body))
    print()


def sendClientUpdate(req):
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
    auth_token = "5dbd8dbd97b0aceab93de491485f3ca7"

    client = Client(account_sid, auth_token)

    recipient = req['toPhone']
    msg = req['content']
    # recipient="+6592340039"
    #msg="Hello from Python!"
    message = client.messages.create(
        # to="+6593877839",
        to=recipient,
        from_="+15405965349",
        body=msg)
    return message.sid


if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveSMS()
