import requests

base_url = 'http://127.0.0.1:8000/api/' 

# Define the user ID of the person to be updated

user_id= 1

# Define the updated data
data = {'name': 'Stephen Kuria', 'age': 36, 'email': 'kevinnehpets@gmail.com'}

# Send a POST request to update the person details
response = requests.post(f'{base_url}{user_id}/update/',data=data)

print(response.json())