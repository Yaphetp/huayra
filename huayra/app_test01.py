# coding: utf-8

import os
import time

def test():
    print 'this is app_test01'
    print os.popen('adb devices')
    print 'test01 over'
    time.sleep(5)
