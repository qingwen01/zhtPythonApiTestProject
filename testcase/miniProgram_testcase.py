import requests
import unittest
from base.base_requests import RunRequests
import os
import json

base_path =os.getcwd() #获取当前文件绝对路径

url1 = "http://119.45.152.126:8081/prod-api/app/token/userLoginV1"
url2 = "http://119.45.152.126:8081/prod-api/system/user/getScAndDpxx"
datas = {
        "client_id": "web",
        "client_secret": "123456",
        "code": "666666",
        "grant_type": "sms_code",
        "scope": "server",
        "username": "15067112912"
}
header1 = {
        "clientType": "Android",
        "Content-Type": "application/json",
        "Authorization":"Bearer f7a0d40b-3046-4f35-ac76-8b6c3ceec2eb"
}

class TestCase02(unittest.TestCase):
    # def setUp(self):
    #     print("程序开始")
    # def tearDown(self):
    #     print("程序结束")

    @classmethod
    def setUpClass(cls):
        print("大程序开始")

    @classmethod
    def tearDownClass(cls):
        print("大程序结束")

    # def test_01(self):
    #     result = RunRequests().run_requests('post', url=url1,data=json.dumps(datas),headers=header1)
    #     self.assertNotIn("200", "result", msg="断言失败")
    #     return result


    def test_02(self):
        result = RunRequests().run_requests('get', url=url2, data=None, headers=header1)
        self.assertNotIn("200","result",msg="断言失败")
        return  result




if __name__ == '__main__':
    unittest.main()