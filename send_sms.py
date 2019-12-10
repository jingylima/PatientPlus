

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe08b7f5ef7f4f302249fbf4a54396c7c'
auth_token = 'ca5b193cf0b2d02092f593a7d4fb99cb'
client = Client(account_sid, auth_token)


def texting():
  message = client.messages \
                  .create(
                       body="High pain intensity detected.",
                       from_='+13343669736',
                       to='+19255650376'
                   )

  print(message.sid)
  
texting()