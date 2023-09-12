import requests

base_url = 'http://127.0.0.1:8000/api/'

user_id = 1

response = requests.post(f'{base_url}{user_id}/delete')

print(response.json)
                         