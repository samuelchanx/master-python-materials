import requests

response = requests.get('https://www.metaweather.com/api/location/2165352')

json = response.json()
response_text = response.text

print(json)
print(response_text)
print(response.headers)
print(json['sun_set'])