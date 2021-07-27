#coding=utf8
import sys
import os
current_path = os.getcwd()
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)
from util.handle_json import read_json,write_value


#获取cookie
def get_cookie_value(cookie_key):
    data = read_json("/config/cookie.json")
    return data[cookie_key]


#写入cookie
def write_cookie(cookie_key,data1):
    json_data = read_json("/config/header.json")   #读取文件内内容
    json_data[cookie_key] = data1                  #将文件内某个字段值换掉
    write_value(json_data)                         #将换掉后的所有值写入文件内





#
# print(write_cookie("Authorization","no"))


