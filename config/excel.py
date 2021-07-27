import json
import sys
import os
current_path = os.getcwd()
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)
from util.handle_excel import handleExcel


excel_data = handleExcel.get_rows_value(i+2)
depend_data = excel_data[3]
method = excel_data[7]
data = excel_data[8]
host = excel_data[5]
path = excel_data[6]