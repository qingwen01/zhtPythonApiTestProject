#coding=utf8
import json
import sys
import os
current_path = os.getcwd()
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)
from base.class_requests import runRequests
from util.handle_excel import handleExcel
from util.handle_ini import handleIni
from util.handle_header import get_header
from util.handle_result import handle_result_message,handle_result_json,get_result_json
from util.handle_dependData import get_dependData
from hyperlink import URL
from util.replace_dependData import replace_get_dependData
import unittest
from ddt import ddt, data, unpack

# testdata = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# print(type(testdata))
testdata = handleExcel.get_excel_data()

@ddt
class mytest(unittest.TestCase):
    def setUp(self):
        print("程序开始")
    def tearDown(self):
        print("程序结束")

    @data(*testdata)
    @unpack
    def test_main_case(self,case_id,is_run,function,depend_data,depend_key,url,path,method,data,cookie_method,is_header,expect_method,expect_result,result,result_data):
        print(case_id,is_run,function,depend_data,depend_key,url,path,method,data,cookie_method,is_header,expect_method,expect_result,result,result_data)



        # case_id,is_run,function,depend_data,depend_key,url,path,method,data,cookie_method,is_header,expect_method,expect_result,result,result_data = data1
        # print("这是用例",case_id,is_run,function,depend_data,depend_key,url,path,method,data,cookie_method,is_header,expect_method,expect_result,result,result_data)
        # rows = handleExcel.get_rows()




        # for i in range(rows):
        #     excel_data = handleExcel.get_rows_value(i+2)
        #     host0 = handleIni.get_value('server', 'host0')
        #     host1 = handleIni.get_value('server', 'host1')
        #     is_run = excel_data[1]
        #     header = None
        #     get_cookie = None
        #     case_id = excel_data[0]
        #     i = handleExcel.get_rows_numble(case_id)
        #     if is_run == 'Y':
        #         depend_data = excel_data[3]
        #         method = excel_data[7]
        #         data = excel_data[8]
        #         host = excel_data[5]
        #         path = excel_data[6]
        #         if host == 0 :
        #             url = host0 + path
        #         else:
        #             url = host1 + path
        #         if depend_data:
        #             depend_key = excel_data[4]
        #             depend_value = get_dependData(depend_data)
        #             if data and method=="post":
        #                 data1 = json.loads(data)
        #                 data1[depend_key] = depend_value
        #                 data = json.dumps(data1)
        #             if data and method=="get":
        #                 url1 = url +data
        #                 data1 = {i[0]: i[1] for i in URL.from_text(url1).query}
        #                 data1[depend_key] = depend_value
        #                 data = replace_get_dependData(data1)
        #         cookie_method = excel_data[9]
        #         is_header = excel_data[10]
        #         expect_method = excel_data[11]
        #         expect_result = str(excel_data[12])
        #         if is_header == "yes":
        #             header = get_header()
        #         if cookie_method == "write":
        #             get_cookie = "yes"
        #         res = runRequests.run_requests(method, url, data, get_cookie, header)   #str
        #         result = json.loads(res)  #将str转换成dict
        #         code = str(result['code'])  #str
        #         message = result['msg']  #str
        #         if expect_method == "codeMesasge":
        #             config_message = handle_result_message(path, code)
        #             if message == config_message:
        #                 handleExcel.excel_write_data(i+2,14,"通过")
        #             else:
        #                 handleExcel.excel_write_data(i+2,14,"失败")
        #             handleExcel.excel_write_data(i+2,15,res)
        #         if expect_method == "errorcode":
        #             if expect_result == code:
        #                 handleExcel.excel_write_data(i+2,14,"通过")
        #             else:
        #                 handleExcel.excel_write_data(i+2,14,"失败")
        #             handleExcel.excel_write_data(i+2,15,res)
        #         if expect_method == "json":
        #             if code == "200":
        #                 status_str = "success"
        #             else:
        #                 status_str = "error"
        #             result0 = get_result_json(path,status_str)  #dict
        #             compare_result = handle_result_json(result0,result)
        #             if compare_result:
        #                 handleExcel.excel_write_data(i+2,14,"通过")
        #             else:
        #                 handleExcel.excel_write_data(i+2,14,"失败")
        #             handleExcel.excel_write_data(i+2,15,res)



if __name__ == '__main__':
    unittest.main()