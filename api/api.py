import requests

weather_api = 'https://www.metaweather.com/api/location/2165352'
# response = requests.get(weather_api)

# # print(response)
# json_response = response.json()
# sunset_time = json_response['sun_set']
# print(sunset_time)

# print(json_response['consolidated_weather'][0]['visibility'])

weather_query_api = 'https://www.metaweather.com/api/location/search/?query=Hong kong'

response = requests.get(weather_query_api)
print(response.json()[0]['woeid'])