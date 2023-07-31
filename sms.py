# Install Twilio library first: pip install twilio
from twilio.rest import Client
# Your Twilio account SID and Auth Token
account_sid = 'ACf117b9bb344f57c6d54f508f0649812'
auth_token = '1fe20059142ec39cc34671beae845e9'
# Create a Twilio client
client = Client(account_sid, auth_token)
# Replace 'to_phone_number' with the recipient's phone number
# Replace 'from_phone_number' with your Twilio phone number
message = client.messages.create(
    body="Stay Healthy, Stay Happy , Stay Curious",
    from_='+15392212899',  # Replace with your Twilio phone number
    to='+919155408330'    # Replace with the recipient's phone number
)

print("Message sent successfully!")
