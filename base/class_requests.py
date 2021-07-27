import json
import requests
from util.handle_cookie import write_cookie

class RunRequests:
    def send_post(self,url,data,get_cookie=None,headers=None):
        res = requests.post(url=url,data=data,headers=headers).json()

        if get_cookie != None:
            # cookie_value_jar = res[data][access_token]
            # cooke_value = res.utils.dict_from_cookiejar(cookie_value_jar)
            cookie_value = "Bearer "+res["data"]["access_token"]
            write_cookie("Authorization",cookie_value)

        return json.dumps(res,ensure_ascii=False, sort_keys=True, indent=2)

    def send_get(self,url,data,get_cookie=None,headers=None):
        res = requests.get(url=url,params=data,headers=headers).json()


        if get_cookie != None:
            cookie_value = "Bearer "+res["data"]["access_token"]
            write_cookie("Authorization",cookie_value)

        return json.dumps(res,ensure_ascii=False, sort_keys=True, indent=2)


    def run_requests(self,method,url,data,get_cookie=None,headers=None):
        res = None
        if method == "post":
            res = self.send_post(url,data,get_cookie,headers)
        elif method == "get":
            res = self.send_get(url,data,get_cookie,headers)
        else:
            print("method值错误！！！")
        # try:
        #     res = json.loads(res)
        # except:
        #     print("这个结果就是text")
        return res


runRequests = RunRequests()


if __name__ == '__main__':
    runRequests = RunRequests()
    url = "http://119.45.152.126:8081/prod-api/app/token/userLoginV1"
    url2 = "http://119.45.152.126:8081/prod-api/system/user/getScAndDpxx"
    data0 = {
        "client_id": "web",
        "client_secret": "123456",
        "code": "666666",
        "grant_type": "sms_code",
        "scope": "server",
        "username": "15067112912"
    }
    cookies = {
        "987d61a5-82db-4bff-b512-2327d1a13450"
    }
    header1 = {
        # "clientType": "Android",
        "Content-Type": "application/json",
        "Authorization":""
    }
    # res = runRequests.run_requests('post', url,data=json.dumps(data0),get_cookie="yes",headers=header1)

    # res = runRequests.run_requests('post', url,data=json.dumps(data0),headers=header1)

    # res = RunRequests().run_requests('get', url=url2, data=None, headers=header1)

    print(res)






