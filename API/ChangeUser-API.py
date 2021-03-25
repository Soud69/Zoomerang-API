import requests
# Importing requests

# Note: We Need Auth Token Fron Login-API.py
# token = json.loads(req.text)["idToken"]

url = "https://us-central1-zoomerang-dcf49.cloudfunctions.net/apiv2/v2/user/username"
# Change API URL

username = input("Username: ")
# Username Input, You Can Use Arabic

data = {"username": username}
# Change API Data

headers = {
	"Host": "us-central1-zoomerang-dcf49.cloudfunctions.net",
	"Content-Type": "application/json",
	"Connection": "keep-alive",
	"Accept": "application/json",
	"User-Agent": "Zoomerang/3.0.16 (com.yantech.zoomerang; build:3; iOS 14.2.1) Alamofire/5.2.2",
	"Authorization": f"Bearer {token}",
	"Accept-Language": "en-US;q=1.0, ar-US;q=0.9",
	"Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8"
	}
# Change API Headers

req = requests.put(url, json=data, headers=headers)
# Change API Requests

if f'username":"{username}"' in req.text:
	print("Changed User Success")
	# User Success Changed

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
