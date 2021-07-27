#coding=utf8
import json
import sys
import os



current_path = os.getcwd() #获取当前文件绝对路径
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  #获取当前文件上上级根目录绝对路径
sys.path.append(base_path)  #将该路径添加到系统变量

#加载json内所有内容
def read_json(file_name=None):
    if file_name == None:
        file_path = base_path+"/config/response.json"
    else:
        file_path = base_path+file_name
    with open(file_path,encoding='UTF-8')as f:
        data = json.load(f)
    return data

#读取文件内某个字段的值
def get_value(key,file_name=None):
    data = read_json(file_name)
    return data.get(key)

#向文件内写入内容
def write_value(data):
    data_value = json.dumps(data)
    with open(base_path+"/config/header.json","w") as f:
        f.write(data_value)


if __name__ == '__main__':
    # print(get_value("/prod-api/app/token/userLoginV1"))
    # print(read_json("/config/header.json"))
    write_value("hahahhahahha")
