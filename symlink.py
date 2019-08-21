#!/usr/bin/python
# encoding:utf-8

import os, shutil


def ln_sf(source, link_name):
    shutil.copytree(source, link_name)


src = "/root/a/"
dst = "/root/v/a"

ln_sf(src, dst)