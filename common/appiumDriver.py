# coding: utf-8

import re
import os
import time
from appium import webdriver
# os.system('adb uninstall io.appium.settings')
# time.sleep(2)
# os.system('adb uninstall io.appium.unlock')
# time.sleep(2)

"""
device_id = ''.join(re.findall('[A-Z0-9]', key1))
device_version = ''.join(re.findall('\d.\d', key3))
app_name = ''.join(re.findall('com\.talk51\.dasheng', key4))
"""
# pc端app地址
# appLocation = os.path.abspath(r'E:\wangping\app\src\apps\release.apk')

# 获取设备ID
readDeviceid = os.popen('adb devices', 'r', -1).readlines()
# 正则表达式匹配出 id 信息
deviceId = str(re.findall(r'^\w*\b', readDeviceid[1])[0:2])

# 读取设备系统版本号
deviceAndroidVersion = os.popen('adb shell getprop ro.build.version.release').read()
deviceVersion = deviceAndroidVersion.strip()
#
# # 删除以前的安装包, 返回success。
# print 'start uninstall app......'
# os.system('adb uninstall ' + 'com.talk51.dasheng')
# # 安装指定目录的apk，返回success
# print 'start install app......'
# os.system('adb install ' + appLocation.strip('\''))

# 读取 APK 的 package 信息，目前固定为com.talk51.dasheng
# appPackageAdb = os.popen('aapt dump badging' + ' ' + appLocation, 'r', -1).readlines()
# appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]

# 自动获取连接到pc的当前设备的必要设备信息
desired_caps = {
    # 'app': appLocation,
    'platformVersion': deviceVersion,
    'deviceName': deviceId,
    # 'deviceName': 'WTKDU16A22003533',
    'appPackage': 'com.talk51.kid',  # 青少儿，成人是'com.talk51.dasheng'
    'platformName': 'Android',
    # 'appActivity': '.activity.SplashActivity', # 老包的activity
    'appActivity': '.core.app.SplashActivity',
    # 'automationName': 'Uiautomator2',
    'automationName': 'appium',
    # 'appWaitActivity': '.activity.dailyTask.user_guide.GuideActivity',
    'noReset': True,
    'recreateChromeDriverSessions': True
    # 设置收到下一条命令的超时时间, 超时appium会自动关闭session, 默认60秒
    # 'newCommandTimeout': '60',
    # 'unicodeKeyboard': True,
    # 'resetKeyboard': True

}

url = 'http://127.0.0.1:4723/wd/hub'


def get_driver():
    driver = webdriver.Remote(url, desired_caps)
    driver.implicitly_wait(30)
    return driver


# def used_driver():
#     global my_driver
#     return my_driver

#
#
# def quit_driver():
#     global MY_DRIVER
#     MY_DRIVER.quit()
