# coding:utf-8
from common.appiumDriver import used_driver  # 使用之前 get_driver替换为used_driver
# from common.appiumDriver import get_driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import Image
from constant import now
import time
import random
import os
import cv2
from matplotlib import pyplot
import numpy as np


class CancelBookError(Exception):
    pass


def if_element_exist(location, value):
    dr = used_driver()
    try:
        if location == 'by_id':
            dr.find_element_by_id(value)
            return True

        if location == 'by_name':
            dr.find_element_by_name(value)
            return True

        if location == 'by_class':
            dr.find_element_by_class_name(value)
            return True

        if location == 'by_xpath':
            dr.find_element_by_xpath(value)
            return True
    except NoSuchElementException:
        print 'No such element found.'
        return False


def if_unlogin():
    dr = used_driver()
    try:
        if dr.find_element_by_id('com.talk51.dasheng:id/btn_login_regi'):
            return True
        else:
            print 'App already logged in. '
            return False
    except NoSuchElementException:
        pass


def login():
    dr = used_driver()
    dr.find_element_by_id('com.talk51.dasheng:id/btn_login_regi').click()
    time.sleep(2)
    dr.find_element_by_id("com.talk51.dasheng:id/et_email").send_keys('15811045057')
    dr.find_element_by_id('com.talk51.dasheng:id/et_password').send_keys('111111')
    dr.find_element_by_id('com.talk51.dasheng:id/btn_login').click()
    time.sleep(10)


def if_logout():
    dr = used_driver()
    if dr.find_element_by_id('com.talk51.dasheng:id/tv_account'):
        return True
    else:
        return False


def logout():
    dr = used_driver()
    dr.find_element_by_id('com.talk51.dasheng:id/tv_account').click()
    # swipe two times
    swipe_up()
    swipe_up()
    time.sleep(1)
    dr.find_element_by_name('设置').click()
    time.sleep(1)
    dr.find_element_by_id('com.talk51.dasheng:id/setting_logout').click()
    dr.find_element_by_id('com.talk51.dasheng:id/button1').click()
    time.sleep(2)


def if_cpad():
    dr = used_driver()
    if if_element_exist('by_id', 'com.talk51.dasheng:id/img'):
        dr.find_element_by_id('com.talk51.dasheng:id/cancel').click()
        time.sleep(1)


def if_ydpage():
    dr = used_driver()
    if if_element_exist('by_id', 'com.talk51.dasheng:id/btn_know'):
        dr.find_element_by_id('com.talk51.dasheng:id/btn_know').click()


def if_hongbao():
    dr = used_driver()
    if if_element_exist('by_id', 'com.talk51.dasheng:id/tv_hongbao_no'):
        dr.find_element_by_id('com.talk51.dasheng:id/tv_hongbao_no').click()


def if_is_booked():
    dr = used_driver()
    if if_element_exist('by_id', 'com.talk51.dasheng:id/confirm'):
        dr.find_element_by_id('com.talk51.dasheng:id/confirm').click()


'''
def find_toast(self, message):
    dr = used_driver()
    """判断toast信息"""
    WebDriverWait(self.dr, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
'''


def find_toast(self, message, timeout=10, poll=0.01):
    dr = used_driver()
    try:
        message = '//*[@text=\'{}\']'.format(message)
        WebDriverWait(self.dr, timeout, poll).until(EC.presence_of_element_located((By.XPATH, message)))
        print 'GET TOAST.....'
        return True
    except Exception as e:
        print 'Get Toast Error :', e
        return False


def get_size():
    dr = used_driver()
    x = dr.get_window_size()['width']
    y = dr.get_window_size()['height']
    print 'width is :', x, 'height is:', y
    # width = 1080, height = 1794
    return x, y


# 向上滑
def swipe_up():
    dr = used_driver()
    s = get_size()
    x1 = int(s[0] * 0.5)
    y1 = int(s[1] * 0.5)
    y2 = y1 - y1 * 0.75
    dr.swipe(x1, y1, x1, y2)


# 向下滑
def swipe_down():
    dr = used_driver()
    s = get_size()
    x1 = int(s[0] * 0.5)
    y1 = int(s[1] * 0.5)
    y2 = y1 + y1 * 0.75
    dr.swipe(x1, y1, x1, y2)


# 向左滑
def swipe_left():
    dr = used_driver()
    s = get_size()
    x1 = int(s[0] * 0.5)
    y1 = int(s[1] * 0.5)
    x2 = int(x1 - x1 * 0.75)
    dr.swipe(x1, y1, x2, y1, 100)  # 滑动时间根据app本身自定义，单位ms


# 向右滑
def swipe_right():
    dr = used_driver()
    s = get_size()
    x1 = int(s[0] * 0.5)
    y1 = int(s[1] * 0.5)
    x2 = int(x1 + x1 * 0.75)
    dr.swipe(x1, y1, x2, y1, 100)


def defined_tap(x1, y1, x2, y2):
    dr = used_driver()
    x1 = float(x1)  # 目标坐标x
    y1 = float(y1)  # 目标坐标y
    x2 = float(x2)  # 当前手机width
    y2 = float(y2)  # 当前手机height
    x3 = float(dr.get_window_size()['width'])  # 测试手机width
    y3 = float(dr.get_window_size()['height'])  # 测试手机height
    x = x1 / x2 * x3
    y = y1 / y2 * y3
    dr.tap([(x, y)])


def random_tap(xs, xe, ys, ye, x1, y1):
    dr = used_driver()
    xs = float(xs)  # 开始目标坐标x
    ys = float(ys)  # 开始目标坐标y
    xe = float(xe)  # 结束目标坐标x
    ye = float(ye)  # 结束目标坐标y
    x1 = float(x1)  # 当前手机width
    y1 = float(y1)  # 当前手机height
    x2 = float(dr.get_window_size()['width'])  # 测试手机width
    y2 = float(dr.get_window_size()['height'])  # 测试手机height
    x = random.uniform(xs / x1 * x2, xe / x1 * x2)  # 产生区间之内的随机整数坐标点x
    y = random.uniform(ys / y1 * y2, ye / y1 * y2)  # 产生区间之内的随机整数坐标点y
    dr.tap([(x, y)])


def kaka(name):
    dr = used_driver()
    all_name = r'E:\wangping\app\src\result\result_' + now + '_' + name + '.png'
    dr.get_screenshot_as_file(all_name)


# delete the files under the 'filedir'
def remove_kaka(file_dir, liked_name, *kw):
    # kw = ''.join(kw)
    # kwargs = ''.join(kwargs.values())
    for root, dirs, files in os.walk(file_dir, topdown=True):
        for filename in files:
            if liked_name in filename:
                os.remove(os.path.join(root, filename))
        # 删除文件夹的操作暂不适用，以后再说
        # for foldername in dirs:
        #     if liked_name in foldername and kwargs == 'folder':
        #         os.rmdir(os.path.join(root, foldername))

# 字符串转2进制
def s2b (string):
    l = []
    for c in string:
        b = bin(ord(c)).replace('0b', '')
        l.append(b)
    print l

# 2进制转字符串, 参数为list
def b2s (binary_list):
    l = []
    for b in binary_list:
        s = chr(int(b, base=2))
        l.append(s)
    print ''.join(l)

def hist_compare(img1_read, img2_read, size = (256, 256)):
    # 图片缩放
    img1_size = cv2.resize(img1_read, size)
    img2_size = cv2.resize(img2_read, size)
    # 转化为直方图的输入数据列表
    img1_hist = cv2.calcHist([img1_size], [0], None, [256], [0.00, 256.00])
    img2_hist = cv2.calcHist([img2_size], [0], None, [256], [0.00, 256.00])
    # 使用matplotlib库绘图,使展示在同一界面可进行比较
    pyplot.plot(range(256), img1_hist, 'r')
    pyplot.plot(range(256), img2_hist, 'b')
    pyplot.show()
    #计算直方图的重合程度
    degree = 0
    for i in range(len(img1_hist)):
        if img1_hist[i] != img2_hist[i]:
            degree = degree + (1 - abs(img1_hist[i] - img2_hist[i]) / max(img1_hist[i], img2_hist[i]))
        else:
            degree = degree + 1
    degree = degree / len(img1_hist)
    return degree

def split_hist_compare(img1_read, img2_read, size = (256, 256)):
    # 分离为三个单独的通道，计算平均值；上面是求三通道的相似值
    img1_size = cv2.resize(img1_read, size)
    img2_size = cv2.resize(img2_read, size)
    sub_img1 = cv2.split(img1_size)
    sub_img2 = cv2.split(img2_size)
    digrees = 0
    for sub1, sub2 in zip(sub_img1, sub_img2):
        digrees = digrees + hist_compare(sub1, sub2)
    degree = digrees / 3
    return degree

# 平均哈希算法计算
def classify_aHash(image1, image2):
    image1 = cv2.resize(image1, (8, 8))
    image2 = cv2.resize(image2, (8, 8))
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    hash1 = getHash(gray1)
    hash2 = getHash(gray2)
    return hanming_distance(hash1, hash2)

# p 哈希算法
def classify_pHash(image1, image2):
    image1 = cv2.resize(image1, (32, 32))
    image2 = cv2.resize(image2, (32, 32))
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # 将灰度图转为浮点型，再进行dct变换
    dct1 = cv2.dct(np.float32(gray1))
    dct2 = cv2.dct(np.float32(gray2))
    # 取左上角的8*8，这些代表图片的最低频率
    # 这个操作等价于c++中利用opencv实现的掩码操作
    # 在python中进行掩码操作，可以直接这样取出图像矩阵的某一部分
    dct1_roi = dct1[0:8, 0:8]
    dct2_roi = dct2[0:8, 0:8]
    hash1 = getHash(dct1_roi)
    hash2 = getHash(dct2_roi)
    return hanming_distance(hash1, hash2)

def getHash(image):
    # 输入灰度图，返回hash
    # 获取图像平均值
    # 每个点与平均值比较
    # 记录1、0到二进制list
    average = np.mean(image)
    hash_list = []
    for cell in range(image.shape[0]):
        for line in range(image.shape[1]):
            if image[cell, line] > average:
                hash_list.append(1)
            else:
                hash_list.append(0)
    return hash_list


def hanming_distance(bin_list1, bin_list2):
    # 计算汉明距离
    hm_value = 0
    for hm_index in range(len(bin_list1)):
        if bin_list1[hm_index] != bin_list2[hm_index]:
            hm_value = hm_value + 1
    return hm_value
