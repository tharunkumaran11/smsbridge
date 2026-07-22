import requests

url = "http://192.168.1.3:8082"

headers = {
    "Authorization": "dee71860-a11f-4f7c-a911-2e37e5c961ac"
}

payload = {
    "to": "+917603828534",
    "message": "Hello! SMSBridge is working 🚀"
}

response = requests.post(
    url,
    json=payload,
    headers=headers
)

print("Status:", response.status_code)
print(response.text)