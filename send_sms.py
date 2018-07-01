# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '#####################################'
auth_token = '######################################'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Hello, This is 'Your Name', How are you?',
         from_='+18284710639',
         to='+####-###-####'
     )

print(message.sid)
