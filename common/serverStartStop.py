# coding=utf-8

import os


# 启动appium
def start_server():
    os.system('appium -a 127.0.0.1 -p 4723 --session-override')


# 任务执行完毕，关闭appium
def stop_server():
    os.system(r'start E:\wangping\app\src\common\stopAppiumServer.bat')
