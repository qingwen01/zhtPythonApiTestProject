#coding=utf8

import json
import sys
import os
current_path = os.getcwd()
print(current_path)
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(base_path)
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
import HTMLTestRunner
import datetime

# testdata = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
# print(type(testdata))
testdata = handleExcel.get_excel_data()


@ddt
class mytest(unittest.TestCase):

    # def __init__(self, *args, **kwargs):
    #     unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        print("程序开始")
    def tearDown(self):
        print("程序结束")

    @data(*testdata)
    def test_main_case(self,data):
        host0 = handleIni.get_value('server', 'host0')
        host1 = handleIni.get_value('server', 'host1')
        is_run = data[1]
        header = None
        get_cookie = None
        case_id = data[0]
        i = handleExcel.get_rows_numble(case_id)
        if is_run == 'Y':
            depend_data = data[3]
            method = data[7]
            parameter = data[8]
            host = data[5]
            path = data[6]
            if host == 0 :
                url = host0 + path
            else:
                url = host1 + path
            if depend_data:
                depend_key = data[4]
                depend_value = get_dependData(depend_data)
                if parameter and method=="post":
                    data1 = json.loads(parameter)
                    data1[depend_key] = depend_value
                    parameter = json.dumps(data1)
                if parameter and method=="get":
                    url1 = url +parameter
                    data1 = {i[0]: i[1] for i in URL.from_text(url1).query}
                    data1[depend_key] = depend_value
                    parameter = replace_get_dependData(data1)
            cookie_method = data[9]
            is_header = data[10]
            expect_method = data[11]
            expect_result = str(data[12])
            if is_header == "yes":
                header = get_header()
            if cookie_method == "write":
                get_cookie = "yes"
            res = runRequests.run_requests(method, url, parameter, get_cookie, header)   #str
            result = json.loads(res)  #将str转换成dict
            code = str(result['code'])  #str
            message = result['msg']  #str
            if expect_method == "codeMesasge":
                config_message = handle_result_message(path, code)

                # if message == config_message:
                #     handleExcel.excel_write_data(i,14,"通过")
                # else:
                #     handleExcel.excel_write_data(i,14,"失败")
                # handleExcel.excel_write_data(i,15,res)
                try:
                    self.assertEqual(message,config_message,msg="失败")
                    handleExcel.excel_write_data(i, 14, "通过")
                except Exception as e:
                    handleExcel.excel_write_data(i, 14, "失败")
                    raise e

            if expect_method == "errorcode":
                # if expect_result == code:
                #     handleExcel.excel_write_data(i,14,"通过")
                # else:
                #     handleExcel.excel_write_data(i,14,"失败")
                # handleExcel.excel_write_data(i,15,res)
                try:
                    self.assertEqual(expect_result, code,msg="失败")
                    handleExcel.excel_write_data(i, 14, "通过")
                except Exception as e:
                    handleExcel.excel_write_data(i, 14, "失败")
                    raise e

            if expect_method == "json":
                if code == "200":
                    status_str = "success"
                else:
                    status_str = "error"
                result0 = get_result_json(path,status_str)  #dict
                compare_result = handle_result_json(result0,result)
                # if compare_result:
                #     handleExcel.excel_write_data(i,14,"通过")
                # else:
                #     handleExcel.excel_write_data(i,14,"失败")
                # handleExcel.excel_write_data(i,15,res)
                try:
                    self.assertTrue(compare_result,msg="失败")
                    handleExcel.excel_write_data(i, 14, "通过")
                except Exception as e:
                    handleExcel.excel_write_data(i, 14, "失败")
                    raise e
            handleExcel.excel_write_data(i, 15, res)


if __name__ == '__main__':
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
    print(now_time)
    case_path = base_path+"/run"
    report_path = base_path+"/report/"+now_time+".html"
    test = unittest.TestLoader().loadTestsFromTestCase(mytest)

    with open(report_path,"wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="qingwen",description="zgbApiTest")
        runner.run(test)
