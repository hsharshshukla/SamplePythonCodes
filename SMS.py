#SIGNUP FOR TWILIO ACCOUNT - https://twilio.com

#Sending Text
from twilio.rest import Client
accountSID = ''
authToken = ''
twilioCli = Client(accountSID,authToken)
myTwilioNumber = '9999999999'
myCellPhone = '99990909999'
#Note from_ has underscore
message = twilioCli.messages.create(body='Mr.Watson', from_ =  myTwilioNumber,to = myCellPhone)

message.status
message.date_created
print(message.date_sent==None)


