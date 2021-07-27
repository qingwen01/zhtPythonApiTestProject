import requests

url = "https://zht.yffsc.com/prod-api/system/file/upload/app/pic"
file = {'file': ('test.jpg', open('D:/test.jpg', 'rb'), 'image/jpg')}

headers2 = {
    "Host": "zht.yffsc.com",
    "Authorization": "Bearer 34bbad51-63b5-40ac-b664-aafb25eabb12",
    "appVersionName": "2.2.5",
    "appVersionCode": "33",
    "refresh_token": "b267079a-62be-42e1-b279-aef6a971fc44",
    "currentLocal": "zh-Hans-CN",
    "clientType": "ios",
    "User-Agent": "YIFA/2.2.5 (com.centralsoft.yfzht; build:33; iOS 14.6.0) Alamofire/5.1.0",
    "Connection": "keep-alive",
}



res = requests.post(url,files=file,headers=headers2,verify=False).json()

print(res)