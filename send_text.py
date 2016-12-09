# https://www.twilio.com/console  UID: snoby@geg!

from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = '<TWILIO_ACC_SID>'
AUTH_TOKEN = '<TWILIO_AUTH_TOKEN>'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
  to = '<OWN_PHONE_NUMBER>',
  from_ = '<TWILIO_PHONe_NUMBER>',
  body = 'Greetings Earthling!',
)
