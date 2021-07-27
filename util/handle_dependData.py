#coding=utf8
import json
import sys
import os
current_path = os.getcwd()
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)
from util.handle_excel import handleExcel
from jsonpath_rw import parse

#分割数据,data类似于zht_oo1>data:banner:id
def split_data(data):
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return  case_id,rule_data



#获取依赖的整条case
def dependData(data,cols=None):
    case_id = split_data(data)[0]
    row_numble = handleExcel.get_rows_numble(case_id,cols)
    data = handleExcel.get_cell_value(row_numble,15)
    return data


#获取依赖字段值
def get_dependData_value(res_data,key):
    json_exe = parse(key)
    madle = json_exe.find(res_data)
    return [match.value for match in madle]

#获取依赖数据
def get_dependData(data):
    res_data = json.loads(dependData(data))
    rule_data = split_data(data)[1] #data.sc_list[*].stalls[*].jyh_xh
    return get_dependData_value(res_data,rule_data)[0]


if __name__ == '__main__':
    # print(split_data("zht_005>data.sc_list[*].stalls[*].jyh_xh")[1])
    # print(dependData("zht_005>data.sc_list[*].stalls[*].jyh_xh"))

    a = {
      "code": 200,
      "data": {
        "TK": "bxiTGTxbl2dtsbl4md54U0HGqcShT8itebWe+UpyFoSfnacZu7MIRLRfJY5Q5qPR",
        "sc_list": [
          {
            "login_url": "http://test1.yffsc.com/zht/uc/login_app.go?TK=l1VjgK9SU2LnDkDAlcBt+7kCJXEAXalVU5p1KoIgZfvzosKBMpoTF1ZdXQOaspggYneAx1cN/HGyrHR3gHTrvw==&JYH_XH=00000000000000096205&_SIGN=KcsUJ9ATmij4/CSaxDLLuw==",
            "msgCount": 11,
            "sc_icon": "http://119.45.152.126:8099/upload/2020/08/04/707e6c26dafb9d6422abf4c1009871c6.png",
            "sc_name": "意法服饰城",
            "sc_xh": "0000000000000000002",
            "stalls": [
              {
                "dpxx_id": "00000000000020040489",
                "dpxx_name": "猪猪测试",
                "jyh_xh": "00000000000000096205",
                "login_url": "http://test1.yffsc.com/zht/uc/login_app.go?TK=l1VjgK9SU2LnDkDAlcBt+7kCJXEAXalVU5p1KoIgZfvzosKBMpoTF1ZdXQOaspggYneAx1cN/HGyrHR3gHTrvw==&JYH_XH=00000000000000096205&_SIGN=KcsUJ9ATmij4/CSaxDLLuw==",
                "msgCount": 11,
                "twh": "1261A"
              }
            ],
            "user_id": 12424109
          },
          {
            "login_url": "http://test1.yffsc.com/zht/uc/login_app.go?TK=l1VjgK9SU2LnDkDAlcBt+61pAh/g1r8glcodbxOLddC+J5zGWcHVpNdn2nAhXGAG8sOLcW9WpkTqSD6qAKt6Uw==&JYH_XH=00000000000000096454&_SIGN=zpD2A2lCmKmaBz+cU1plRw==",
            "msgCount": 0,
            "sc_icon": "http://119.45.152.126:8099/upload/2020/07/26/d004b25e75135c9eb42a75694c37a3c4.png",
            "sc_name": "中洲女装城",
            "sc_xh": "0000000000000000006",
            "stalls": [
              {
                "dpxx_id": "00000000000020051964",
                "dpxx_name": "哈当",
                "jyh_xh": "00000000000000096454",
                "login_url": "http://test1.yffsc.com/zht/uc/login_app.go?TK=l1VjgK9SU2LnDkDAlcBt+61pAh/g1r8glcodbxOLddC+J5zGWcHVpNdn2nAhXGAG8sOLcW9WpkTqSD6qAKt6Uw==&JYH_XH=00000000000000096454&_SIGN=zpD2A2lCmKmaBz+cU1plRw==",
                "msgCount": 0,
                "twh": "8002"
              }
            ],
            "user_id": 12424109
          }
        ]
      },
      "msg": "操作成功"
    }
    # print(type(a))
    # print(get_dependData_value(a,"data.sc_list[*].stalls[*].jyh_xh"))
    # print(get_dependData_value(a,"data.sc_list[*].stalls[*].jyh_xh")[0])
    #
    print(get_dependData("zht_005>data.sc_list[*].stalls[*].jyh_xh"))



