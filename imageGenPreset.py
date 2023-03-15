import requests

url = "https://api.tryleap.ai/api/v1/images/models/e0cc3190-882d-46e1-8d14-f99a58b91336/inferences"
payload = {
    "prompt": "a picture of @biden going to the candy store",
    "steps": 25,
    "width": 512,
    "height": 512,
    "numberOfImages": 1
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer 0ba4424b-4dce-44c7-9b6e-c58e6d55b6bb"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)