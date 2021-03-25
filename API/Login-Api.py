import requests
import json 
# Importing json And requests 

url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyAZyyldZdaECkbp9vEr0IkFFfghSgtv20U"
# Login API URL

headers = {
	"Host": "www.googleapis.com",
	"Content-Type": "application/json",
	"Accept": "*/*",
	"X-Ios-Bundle-Identifier": "com.yantech.zoomerang",
	"Connection": "keep-alive",
	"X-Client-Version": "iOS/FirebaseSDK/6.9.2/FirebaseCore-iOS",
	"User-Agent": "FirebaseAuth.iOS/6.9.2 com.yantech.zoomerang/3.0.16 iPhone/14.2.1 hw/iPhone13_3",
	"Accept-Language": "en",
	"Accept-Encoding": "gzip, deflate, br"
	} 
# Login API Headers

email = input("Email: ") 
# Email Input
password = input("Password: ") 
# Password Input

data = {
	"email": email,
	"password": password,
	"returnSecureToken": "true"
}
# Login API Data

req = requests.post(url, json=data, headers=headers)
# Login API Request

if "INVALID_EMAIL" in req.text:
	print("Invalid Email, Try Again")
	# Wrong Email

elif "EMAIL_NOT_FOUND" in req.text:
	print("Email Not Used, Try Again")
	# Email Not Used

elif "INVALID_PASSWORD" in req.text:
	print("Bad Password, Try Again")
	# Weak Password

elif '"idToken":' in req.text:
	print("Login Success")
	token = json.loads(req.text)["idToken"]
	print(req.text)
	# Login Success And Parse Login Token

else:
	print("Error !")
	print(req)
	print(req.text)
	# Error or Something Wrong
