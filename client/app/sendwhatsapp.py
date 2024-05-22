# sendwhatsapp.py
# Description: This script sends a message to a whatsapp number using the Twilio API


from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "your_account_sid"
# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="whatsapp:+14155238886",
    from_="whatsapp:+14155238886",
    body="Hello from Python!")