""" 
Goals: Use Python requests to call the add contacts to Send Grid
API documentation: https://sendgrid.api-docs.io/v3.0/contacts/add-or-update-a-contact

After calling the API, you should see the added contacts in SendGrid Contacts
"""

import requests
import json

# TODO: SENDGRID
url = 'https://MYAPI'

# TODO: Some body data to fill in
body_data = {}

# TODO: Some API KEY
headers = {'Authorization': 'Bearer My_API_KEY'}

# Convert body data to string
json_in_string = json.dumps(body_data)
response = requests.put(url, data=json_in_string, headers=headers)

# Check if the response is OK
print(response.status_code)
