#!/usr/bin/env python
#encoding:utf-8
#执行该脚本会配置asp环境、supervisord、nginx环境，只需上传项目包,开启防火墙使用端口,添加supervisord配置文件即可
import os
import subprocess
import shutil
import urllib

# server酱发送消息
def server_message(title, content):
    server_api = "https://sc.ftqq.com/SCU4540T76fc41872bbeff3016cab71ac402503b5853639d939d7.send"
    values = {
    "text": title,
    "desp": content
    }
    urllib.urlopen(server_api, data=urllib.urlencode(values))

#修改为163镜像源和update不升级内核
def server_update(yum_163_config, yum_update_config):
    if os.access(yum_163_config, os.F_OK):
       pass
    else:
        python_shell("mv CentOS-Base.repo CentOS-Base.repo.backup", "/etc/yum.repos.d/")
        urllib.urlretrieve("http://mirrors.163.com/.help/CentOS7-Base-163.repo", "/etc/yum.repos.d/CentOS7-Base-163.repo")
        python_shell("yum clean all && yum makecache")
    with open(yum_update_config, "r+") as f:
        f.seek(0)
        kernel_file = "exclude=centos-release*\n"
        if kernel_file in f.readlines():
            pass
        else:
            f.write("""exclude=kernel*
exclude=centos-release*
            """)

#关闭selinux
def disable_selinux(selinux_config):
    #subprocess.call("setenforce=0")
    python_shell("setenforce=0")
    file_data = ""
    with open(selinux_config) as f:
        old_selinux = "SELINUX=enforcing"
        new_selinx = "SELINUX=disabled"
        for line in f.readlines():
            if old_selinux not in line:
                pass
            else:
                line = line.replace(old_selinux, new_selinx)
            file_data += line
    with open(selinux_config, "w") as f:
        f.write(file_data)

#追加一行文件内容
def add_one_file(file_path, add_content):
    with open(file_path, "a+") as f:
        f.seek(0)
        if add_content in f.readlines():
            pass
        else:
            f.write(add_content)

#修改文件内容
def mod_file(filename, file_content):
    with open(filename, "w+") as f:
        f.write(file_content)

#追加两行文件内容
def add_two_file(file_path, add_content):
    with open(file_path, "a+") as f:
        f.seek(0)
        file_content = "hard nofile 102400\n"
        if file_content in f.readlines():
            pass
        else:
            f.write(add_content)

#执行shell操作
def python_shell(commod, pathname="/root"):
    subprocess.call(commod, shell=True, cwd=pathname)
    # p = subprocess.Popen(commod, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout, stderr = p.communicate()
    # if p.returncode != 0:
    #     return p.returncode, stderr
    # return p.returncode, stdout

#安装配置supervisord
def supervisord(config_path, service_file):
    config_name = config_path + "supervisord.conf"
    if os.access(config_name, os.F_OK):
        pass
    else:
        python_shell("easy_install supervisor")
        shutil.rmtree(config_path, ignore_errors=True)
        os.makedirs(os.path.join(config_path, "conf.d"))
        python_shell("echo_supervisord_conf > /etc/supervisor/supervisord.conf")
    with open(config_name, "a+") as f:
        f.seek(0)
        line = "files = conf.d/*.conf\n"
        if line in f.readlines():
            pass
        else:
            f.write("[include]\n" + line)
    if os.access(service_file, os.F_OK):
        pass
    else:
        with open(service_file, "w+") as f:
            f.write("""# dservice for systemd (CentOS 7.0+)
# by ET-CS (https://github.com/ET-CS)
[Unit]
Description=Supervisor daemon
After=network.service

[Service]
Type=forking
ExecStart=/usr/bin/supervisord -c /etc/supervisor/supervisord.conf
ExecStop=/usr/bin/supervisorctl shutdown
ExecReload=/usr/bin/supervisorctl reload
KillMode=process
Restart=on-failure
RestartSec=42s

[Install]
WantedBy=multi-user.target
        """)

def main():
    #server_message("你好","服务器")
    server_update("/etc/yum.repos.d/CentOS7-Base-163.repo", "/etc/yum.conf")
    disable_selinux("/etc/selinux/config")
    python_shell("rpm -Uvh https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm")
    python_shell("yum install epel-release -y")
    python_shell("yum update -y")
    python_shell("yum install dotnet-sdk-2.2 -y")
    python_shell("yum install libgdiplus-devel -y")
    python_shell("ln -sf libdl-2.*.so libdl.so", "/usr/lib64")
    python_shell("yum install redis -y")
    python_shell("systemctl start redis && systemctl enable redis")
    python_shell("ulimit -n 102400")
    add_two_file("/etc/security/limits.conf", "soft nofile 102400\nhard nofile 102400\n")
    add_one_file("/etc/sysctl.conf", "fs.inotify.max_user_instances = 102400\n")
    mod_file("/proc/sys/fs/inotify/max_user_instances", "102400")
    python_shell("yum install python-setuptools -y")
    supervisord("/etc/supervisor/", "/usr/lib/systemd/system/supervisord.service")
    python_shell("yum install nginx -y && systemctl start nginx")
    python_shell("firewall-cmd --zone=public --add-port=80/tcp --permanent")
    python_shell("systemctl restart firewalld")
    server_message("环境已部署完成", "请查看服务器")

if __name__ == "__main__":
    main()