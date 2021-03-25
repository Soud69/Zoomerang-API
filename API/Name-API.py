import requests
# Importing requests

# Note: We Need Auth Token Fron Login-API.py
# token = json.loads(req.text)["idToken"]

url = "https://us-central1-zoomerang-dcf49.cloudfunctions.net/apiv2/v2/user/update"
# Full Name API URL

name = input("Name: ")
# Full Name Input

data = {"full_name": name}
# Full Name API Data

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
# Full Name API Headers

req = requests.put(url, json=data, headers=headers)
# Full Name API Requests

if f'full_name":"{name}"' in req.text:
	print("Changed Name Success")
	# Full Name Success Changed

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
