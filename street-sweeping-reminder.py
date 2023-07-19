# Twilio to send text message and a call
from twilio.rest import Client
import os
# .env for Twilio credentials
from dotenv import load_dotenv
from datetime import datetime
import time

# Loading .env with secrets
load_dotenv()

# Twilio credentials and client set up
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_NUMBER']
my_number = os.environ['PERSONAL_NUMBER']

client = Client(account_sid, auth_token)


weekday = datetime.today().weekday()
print(weekday)


def send_message(instruction):
    
    # Text message to be sent
    message = client.messages \
        .create(
            body=f"{instruction}",
            from_=twilio_number,
            to=my_number
        )
    # Twilio message log
    print(message.sid)

    # Text confirmation
    print("Success")


client = Client(account_sid, auth_token)


weekday = datetime.today().weekday()
print(weekday)
if weekday == 4:
    instruction = "Tomorrow is Thursday, street sweeping will be on the other side of the street, make sure to park on the near side tonight!"
    send_message(instruction)
else:
    instruction = "Tomorrow is Friday, street sweeping will be on the near side of the street, make sure to park on the other side tonight!"
    send_message(instruction)

 


