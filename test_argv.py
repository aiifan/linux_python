#!/usr/bin/env python
# coding: utf-8
#通过命令行查看文件是否存在
# sys.argv保存了所有的命令行参数，第一个元素是命令行程序的名称，其余的命令行参数以字符串的形式保存


from __future__ import print_function
import os
import sys
def main():
    #防止没有传递参数
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + "does not exists")
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + "is not accessible")
    else:
        print(filename + "is accessible")
if __name__ == "__main__":
    main()

