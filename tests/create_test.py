import requests

url = "http://127.0.0.1:8000/api/"

data = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30
}

response = requests.post(url, data=data)

if response.status_code == 201:
    print("Person created successfully!")
else:
    print(f"Error creating person. Status code: {response.status_code}")
