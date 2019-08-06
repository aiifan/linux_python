#!/bin/bash
#encoding:utf-8

old_yum_config="/etc/yum.repos.d/CentOS-Base.repo"
if [ -e $old_yum_config ]; then
    cd "/etc/yum.repos.d/"
    mv $old_yum_config 'CentOS-Base.repo.backup'
    curl -O http://mirrors.163.com/.help/CentOS7-Base-163.repo
    yum clean all
    yum makecache
fi


