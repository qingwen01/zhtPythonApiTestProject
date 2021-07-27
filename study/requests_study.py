import requests,json


get_url="https://zht.yffsc.com/prod-api/system/zht/menu/app/list?jyhXh=00000000000000098474&scXh=0000000000000000002"
post_url="https://zht.yffsc.com/prod-api/app/token/userLoginV1"
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

headers1 = {
    "clientType": "ios",
    # "Content-Type": "application/json",
}

datas = {
    "grant_type": "sms_code",
	"client_secret": "123456",
	"scope": "server",
	"username": "13735887043",
	"client_id": "web",
	"code": "666666"
}

get_res = requests.get(get_url,headers=headers2,verify=False).json()
get_res = json.dumps(get_res,indent=2)

print(get_res)
#
# post_res = requests.post(post_url,headers=headers1, json=datas,verify=False).json()
# post_res = json.dumps(post_res,indent=2)
#
# print(post_res)


# print(type(post_res))