#encoding:utf-8
import os


yum_conf_site = "keepcache=0\n"
yum_conf_path = "yum.conf"
kernel_no_up = "exclude=kernel*\n"
release_no_up = "exclude=centos-release*\n"

file = open(yum_conf_path,'r')
content = file.read()
post = content.find(yum_conf_site)
if post != -1:
    content = content[:post+len(yum_conf_site)]+kernel_no_up+release_no_up+content[post+len(yum_conf_site):]
    file = open(yum_conf_path,'w')
    file.write(content)
file.close()