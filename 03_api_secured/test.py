import os
from sendgrid import SendGridAPIClient
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# message = Mail(
#     from_email='cchin.samuel@gmail.com',
#     to_emails='cchin.samuel@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python Hello XD</strong>')
# try:
    # sg = SendGridAPIClient('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')
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

sg = SendGridAPIClient('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')
data = [
  {
    "age": 25,
    "email": "example@example.com",
    "first_name": "",
    "last_name": "User"
  },
  {
    "age": 25,
    "email": "example2@example.com",
    "first_name": "Example",
    "last_name": "User"
  }
]
response = sg.client.contactdb.recipients.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)


""" 
import http.client

conn = http.client.HTTPSConnection("api.sendgrid.com")

payload = "{\"contacts\":[{\"address_line_1\":\"string (optional)\",\"address_line_2\":\"string (optional)\",\"city\":\"string (optional)\",\"country\":\"string (optional)\",\"email\":\"hi@samuelchan.xyz\",\"first_name\":\"string (optional)\",\"last_name\":\"string (optional)\",\"postal_code\":\"string (optional)\",\"state_province_region\":\"string (optional)\",\"custom_fields\":{}}]}"

headers = {
    'authorization': "Bearer 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",
    'content-type': "application/json"
    }

conn.request("PUT", "/v3/marketing/contacts", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
"""