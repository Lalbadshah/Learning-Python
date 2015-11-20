from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ENTER STUFF HERE"
auth_token  = "ENTER STUFF HERE"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Mohobbat Hai Mirchi Sanam!",
    to="+918110020607",    # Replace with your phone number
    from_="+16692362136") # Replace with your Twilio number
print message.sid
