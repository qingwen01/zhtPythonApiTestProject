#coding=utf8
import sys
import os
import configparser


current_path = os.getcwd() #获取当前文件绝对路径
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  #获取当前文件上上级根目录绝对路径
sys.path.append(base_path)  #将该路径添加到系统变量

# file_path = base_path+"/config/defined_variables.ini"
# config = configparser.ConfigParser()
# config.read(file_path, encoding="utf-8")
# data = config.get('db','db_host')
# print(data)

class HandleIni:

    #加载defined_variables.ini文件
    def load_ini(self):
        file_path = base_path + "/config/defined_variables.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8")
        return cf

    #获取ini文件里面的内容
    def get_value(self,section0,key0):
        if section0 == None:
            section0 = 'server'
        data = self.load_ini().get(section=section0,option=key0)
        return data

handleIni = HandleIni()
if __name__ == '__main__':
    handleIni = HandleIni()
    print(handleIni.get_value('server','host'))




