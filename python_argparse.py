#!/usr/bin/env python
#coding:utf-8
# argparse解析命令行参数
from __future__ import print_function
import argparse
#ArgumentParser类初始化函数，有多个参数：  description是程序的描述信息，即帮助信息前的文字
"""
❑name/flags：参数的名字；
❑action：遇到参数时的动作，默认值是store；
❑nargs：参数的个数，可以是具体的数字，或者是“+”号与“*”号。其中，“*”号表示0或多个参数，“+”号表示1或多个参数；
❑const action和nargs：需要的常量值；
❑default：不指定参数时的默认值；
❑type：参数的类型；
❑choices：参数允许的值；
❑required：可选参数是否可以省略；
❑help：参数的帮助信息；
❑metavar：在usage说明中的参数名称；
❑dest：解析后的参数名称。
"""
#parser = argparse.ArgumentParser()
def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument("--host", action="store", dest="server", default="localhost", help="connect to host")
    parser.add_argument("-t", action="store_true", default=False, dest="boolean_switch",help="ser a switch to true")
    return parser.parse_args()

def main():
    parser = _argparse()
    print(parser)
    print("host = ",parser.server)
    print("boolean_switch=", parser.boolean_switch)
if __name__ == "__main__":
    main()