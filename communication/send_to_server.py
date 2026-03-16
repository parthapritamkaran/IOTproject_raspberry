

import requests

SERVER_URL = "https://iotproject-1yzr.onrender.com/api/gps-data"

def send_data(payload):

    try:

        response = requests.post(SERVER_URL, json=payload)

        print("Data sent:", response.status_code)

    except Exception as e:

        print("Error sending data:", e)