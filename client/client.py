import requests

endpoint = 'http://127.0.0.1:8000/api'

get_request = requests.get(endpoint, params={'abc': 123}, json={"message": "echo get request"})
print(get_request.text)
print(get_request.status_code)
print(get_request.json)
