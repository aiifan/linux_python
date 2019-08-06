#coding:utf-8

import urlparse
import urllib
import urllib2

def server_message(title, content):
    server_api = "https://sc.ftqq.com/SCU4540T76fc41872bbeff3016cab71ac402503b5853639d939d7.send"
    values = {
        "text": title,
        "desp": content
    }
    data = urllib.urlencode(values)
    req = urllib.urlopen(server_api,data)
    # req = urllib2.Request(server_api, data)
    # message = urllib2.urlopen(req)
    # print message
if __name__ == "__main__":
    server_message("你好7", "服务器")