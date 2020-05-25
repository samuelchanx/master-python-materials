""" 
Project Tasks:
Print movie names whose movie years are after 2005, by updating codes inside function `find_movies_after()`
Hint: the movie names should be stored inside `movies_after_2005` array
"""

import requests

# TODO: Update my API key
api_key = 'myapikey'
movie_title = 'harry potter'
response = requests.get('http://www.omdbapi.com/?apikey=%s&s=%s' % (api_key, movie_title))

response_json = response.json()
harry_potter_results = response_json['Search']

# print the number of harry potter results
print(len(harry_potter_results))

movies_after_2005 = []

# Find movies after `year_after` 
# TODO: Update codes inside function to make it work
def find_movies_after(year_after):
  for movie in harry_potter_results:
    movie_year = movie['Year']

    if int(movie_year) > year_after:
      movies_after_2005.append(movie_year)

find_movies_after(2005)
print(movies_after_2005)
