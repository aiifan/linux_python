#!/usr/bin/env python
# coding:utf-8
#解析配置文件
import ConfigParser
cf = ConfigParser.ConfigParser(allow_no_value=True)
print(cf.read("my.ini"))
print(cf.sections())  #返回一个包含所有章节的列表
print(cf.has_section("client"))   #判断章节是否存在  ture\false
print(cf.options("client"))   #返回一个包含章节下所有选项的列表
print(cf.has_option("client", "user"))   #判断某个选项是否存在
print(cf.get("client", "host"))     # 获取选项的值，还可以使用getboolean\getinit\getfloat   
print(cf.getint("client", "port"))
#items:以元组形式返回所有选项

#修改配置文件
"""
remove_section：删除一个章节；
add_section：添加一个章节；
remote_option：删除一个选项；
set:添加一个选项；
write将configparser对象中的数据保存到文件中
"""
cf.remove_section("client")
cf.add_section("mysqll")
cf.set("mysqll","host","127.0.0.1")
cf.set("mysqll","port","3306")
cf.write(open("my_copy.ini", "w"))
