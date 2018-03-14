# coding=utf-8

import os


# 启动appium
def start_server():
    os.system('start E:\wangping\git-github01\common\startAppiumServer.bat')


# 任务执行完毕，关闭appium
def stop_server():
    os.system(r'start E:\wangping\app\src\common\stopAppiumServer.bat')
