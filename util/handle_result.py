#coding=utf8
import sys
import os
current_path = os.getcwd()
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)
from util.handle_json import get_value
from deepdiff import DeepDiff

#获取返回结果message
def handle_result_message(url,code):
    data = get_value(url,"/config/code_message.json")
    if data != None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None

#获取返回结果message
def get_result_json(url,status):
    data = get_value(url, "/config/result.json")
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None

#校验json格式
def handle_result_json(dict1,dict2):
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        compare_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        if compare_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False


if __name__ == '__main__':

    print(handle_result_message("/prod-api/app/token/userLoginV1","600"))
    #
    # a = {"Object": {
    #     "code": "0",
    #     "message": "success"
    # },
    #     "message": "0",
    #     "timestamp": "success"
    # }
    #
    # b = {"Object": {
    #     "code": "0",
    #     "message": "failure"
    # },
    #     "message": "success",
    #     "timestamp": "1614301293"
    # }
    # print(handle_result_json(a, b))