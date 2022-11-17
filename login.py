import requests

session = requests.session()

headers = {
	"POST": "/identitytoolkit/v3/relyingparty/sendVerificationCode?key=AIzaSyA5admOQ2tW93Tg9GRm4Jh2TbRojxahQqI HTTP/1.1",
	"Host": "www.googleapis.com",
	"Content-Type": "application/json",
	"Accept": "/",
	"X-Ios-Bundle-Identifier": "com.eddress.gorillas",
	"Connection": "keep-alive",
	"X-Client-Version": "iOS/FirebaseSDK/8.8.0/FirebaseCore-iOS",
	"User-Agent": "FirebaseAuth.iOS/8.8.0 com.eddress.gorillas/1.9.41 iPhone/15.5 hw/iPhone12_1",
	"Accept-Language": "nl",
	"Content-Length": "207",
	"Accept-Encoding": "gzip, deflate, br"
}

json = {
	"iosReceipt": "AEFDNu-qx3Ihec2i21RH9ond90hUZVEMJUnlFm8nTRkfqbQ_GMmg5QZxvS87dn5Jhz7xXV5q4DIa_no2bZlFCvMuKO4LNCQmYI7VlLuZ4EaJTgnptHKSJ6nczN0T5coMJg",
	"iosSecret": "oL6nfsT2uZyQ08hY",
	"phoneNumber": "+31642677788"
}

response = session.post("https://www.googleapis.com/identitytoolkit/v3/relyingparty/sendVerificationCode?key=AIzaSyA5admOQ2tW93Tg9GRm4Jh2TbRojxahQqI", headers=headers, json=json)

print(response.text)

