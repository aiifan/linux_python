#!/bin/bash
#encoding:utf-8

yum_conf_site="distroverpkg=centos-release"
yum_conf="/etc/yum.conf"
kernel_up="exclude=kernel*"
release_up="exclude=centos-release*"
yum_conf_bak="/etc/yum.conf.bak"

if [ -e $yum_conf_bak ]; then
    echo ""${yum_conf_bak}"已存在"    
else
    cp ${yum_conf} "${yum_conf_bak}"
    echo ""${yum_conf}"已备份"
fi

kernel=grep "${kernel_up}" "${yum_conf}"
release=grep "${release_up}" "${yum_conf}"
if [[ $kernel -eq $kernel_up ]] && [[ $release -eq $release_up ]]; then
    echo '无需修改'
elif [[ $kernel -eq $kernel_up ]] 


else
    line=`cat -n ${yum_conf} | grep ${yum_conf_site} | awk '{print $1}'`
    sed -i "${line}a\ ${release_up}" ${yum_conf}
    sed -i "${line}a\ ${kernrl_up}" ${yum_conf}
fi
