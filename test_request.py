import requests

url = "http://127.0.0.1:8000/ask-question"
headers = {
    "Content-Type": "application/json",
    "X-Token": "supersecret"
}
data = {"user_question": "How do I reset my password?"}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
