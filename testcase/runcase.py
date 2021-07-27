import unittest
from base.base_requests import RunRequests
import os
import sys
import json

from testcase.zhtApp_testcase import TestCase01
from testcase.miniProgram_testcase import TestCase02

base_path = os.getcwd() #获取当前文件绝对路径
sys.path.append(base_path) #将该路径添加到系统变量


discover = unittest.defaultTestLoader.discover(base_path,pattern="*_testcase.py")
unittest.TextTestRunner().run(discover)
print(discover)


