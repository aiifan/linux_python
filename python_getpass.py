#!/usr/bin/env python
#coding:utf-8
#getpass  读取密码
from __future__ import print_function
import getpass
user = getpass.getuser() #从环境变量获取用户名
passwd = getpass.getpass("your passwprd: ")
print(user, passwd)