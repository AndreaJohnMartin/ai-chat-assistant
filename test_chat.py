import requests

url = "http://127.0.0.1:5000/chat"
data = {"message": "Tell me a joke."}

response = requests.post(url, json=data)

print("Assistant says:", response.json())
