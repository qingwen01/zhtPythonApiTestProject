#coding=utf8
import sys
import os
current_path = os.getcwd()
base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_path)


def replace_get_dependData(data):
    e = []
    for m, v in data.items():
        c = "=".join([m, v])
        e.append(c)
    d = "&".join(e)
    return d


if __name__ == '__main__':
    data={"name":"哈哈","age":"30","sex":"女"}
    print(replace_get_dependData(data))