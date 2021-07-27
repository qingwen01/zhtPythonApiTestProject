# coding=utf8
import sys
import os
current_path = os.getcwd()
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)
from util.handle_json import read_json

def get_header():
    data = read_json("/config/header.json")
    return data


if __name__ == '__main__':
    print(get_header())