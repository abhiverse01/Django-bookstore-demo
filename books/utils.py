# books/utils.py

import requests

def fetch_external_data(url):
    response = requests.get(url)
    return response.json()
