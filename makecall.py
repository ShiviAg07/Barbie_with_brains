import requests
import roza

url = "wss://webliveroom818813303-api.coolzcloud.com/ws"

payload = {
  "method": "customCallout",
  "customCallout": {
    "cli": "+916397589852",
    "destination": {
      "type": "number",
      "endpoint": "+919058376683"
    },
    "maxDuration":"30"
    
  }
}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers, auth=('Shivangi Agrawal','Shivangi07'))

data = response.json()
print(data)