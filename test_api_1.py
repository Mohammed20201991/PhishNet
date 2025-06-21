import requests

# API endpoint
API_URL = 'http://localhost:5000/predict'

# JSON payload
data = {
    "directory": "D:/work/Detecting-Phishing-Attack-using-ML-DL-Models-main/Testing-mails"
}

# Send POST request
try:
    response = requests.post(API_URL, json=data)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)