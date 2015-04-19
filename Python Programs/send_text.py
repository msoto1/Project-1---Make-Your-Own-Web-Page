from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC45d5a966cfa19a5ef5555eae5b4964c5"  #My SID acct.
auth_token  = "22a2600b8177cfc6d42cd8508664d0a3"    #My Token
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",  #Enter text message
    to="+17602017523",    # Replace with your phone number - number to send text to
    from_="+17608914069") # Replace with your Twilio number - your number from twilio
print message.sid
