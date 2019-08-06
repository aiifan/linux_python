#!/usr/bin/python
# coding:utf-8
#标准输入读取内容
"""
filename: 当前正在读取的文件名；
fileno: 文件的描述符；
filelineno：正在读取的行是当前文件的第几行；
isfirstline：正在读取的行是否是当前文件的第一行
isistdin fileinput: 正在读取文件还是直接操你个标准输入读取内容
"""

from __future__ import print_function
import fileinput
for line in fileinput.input():
    meta = [fileinput.filename(), fileinput.fileno(), fileinput.filelineno(),fileinput.isfirstline(), fileinput.isstdin()]
    print(*meta, end="")
    print(line, end="")
