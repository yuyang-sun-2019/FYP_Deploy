#AC6fa56acf5f90ea0eaff9173c1b4c50cb
#14269c6de9ff7c70612ebeda36d05116

from twilio.rest import Client

account_sid = 'AC6fa56acf5f90ea0eaff9173c1b4c50cb'
auth_token = '14269c6de9ff7c70612ebeda36d05116'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+6583193088',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+6583193088'
)

print(message.sid)

# from twilio.rest import Client
#
# account_sid = 'AC6fa56acf5f90ea0eaff9173c1b4c50cb'
# auth_token = '14269c6de9ff7c70612ebeda36d05116'
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   to='whatsapp:+6583193088'
# )
#
# print(message.sid)
