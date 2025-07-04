import requests
import os
from test_dict import test_dictionary

# API
MOVIEDB_API = os.getenv('MOVIEDB_API_KEY')
MOVIEDB_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIEDB_TOKEN = os.getenv('MOVIEDB_API_TOKEN')
url = "https://api.themoviedb.org/3/movie/762975"

import requests

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {MOVIEDB_TOKEN}"
}

params = {
    # "movie_id": 762975,
    "language": "en-US"
}

response = requests.get(url, headers=headers, params=params)
output = response.json()
# results = output['results']

print(output)
# base_url = 'https://image.tmdb.org/t/p/w500'  # or w780, original, etc.
#
#
#
# for result in results:
#     backdrop_path = result['backdrop_path']
#     img_url = base_url + backdrop_path
#     print(result)