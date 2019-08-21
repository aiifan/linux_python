#!/bin/python
#encoding:utf-8

from __future__ import print_function
import  subprocess
import threading
from Queue import Queue, Empty

def call_ping(ip):
    if subprocess.call(["ping", "-c", "1", ip]):
        print("{} is alive".format(ip))
    else:
        print("{} is unreacheable".format(ip))

def is_reacheable(q):
    try:
        while True:
            ip = q.get_nowait()
            call_ping(ip)
    except Empty:
        pass


if __name__ == '__main__':
    q = Queue()
    with open("ips.txt") as f:
        for line in f:
            q.put(line)
    threads = []
    for i in range(10):
        thr = threading.Thread(target=is_reacheable, args=(q, ))
        thr.start()
        threads.append(thr)
    for thr in threads:
        thr.join()