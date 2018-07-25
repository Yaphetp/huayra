# coding=utf-8
from common.appiumDriver import get_driver  # 使用之前 get_driver替换为used_driver
# from common.appiumDriver import get_driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PIL import ImageGrab, Image
from constant import now, locate
import time
import random
import os
import cv2
from matplotlib import pyplot
import numpy as np
import logging

appium_id = 'appium_id'
appium_ids = 'appium_ids'
appium_name = 'appium_name'
appium_nameLike = 'appium_nameLike'
appium_nameLikeIndex = 'appium_nameLikeIndex'
appium_className = 'appium_className'
appium_xpath = 'appium_xpath'
appium_accessibility = 'appium_accessibility'

logging.basicConfig(level=logging.INFO, format='%(asctime)s >>> %(levelname)s >>> %(message)s')
logger = logging.getLogger(__name__)


def get_element(driver, location, value, *index):
    # 通过id定位
    if location == appium_id:
        element = driver.find_element_by_id(value)
        return element
    # 通过id's 定位
    elif location == appium_ids:
        element = driver.find_elements_by_id(value)[index[0]]
        return element
    # 通过name定位
    elif location == appium_name:  # 新版本通过name定位，只能通过如下方法
        # 如下两种方式都可以实现
        # element = driver.find_element_by_android_uiautomator('text(\"'+value+'\")')
        element = driver.find_element_by_android_uiautomator('new UiSelector().text("'+value+'")')
        return element

    # 通过name模糊匹配
    elif location == appium_nameLike:  # 新版本通过name定位，只能通过如下方法
        # 如下两种方式都可以实现
        # element = driver.find_element_by_android_uiautomator('text(\"'+value+'\")')
        element = driver.find_element_by_android_uiautomator('new UiSelector().textContains("'+value+'")')
        return element

    # 通过name模糊匹配,外加index定位
    elif location == appium_nameLikeIndex:  # 新版本通过name定位，只能通过如下方法
        # 如下两种方式都可以实现
        # element = driver.find_element_by_android_uiautomator('text(\"'+value+'\")')
        element = driver.find_elements_by_android_uiautomator('new UiSelector().textContains("'+value+'")')[index[0]]
        return element
    # 通过classname定位
    elif location == appium_className:
        element = driver.find_element_by_class_name(value)
        return element
    # 通过accessibility定位（content-desc）,value输入content-desc的内容即可。
    elif location == appium_accessibility:
        # element = driver.find_element_by_accessibility_id(value)
        element = driver.find_element_by_android_uiautomator('new UiSelector().description("'+value+'")')
        return element
    # 通过xpath定位
    elif location == appium_xpath:
        element = driver.find_element_by_xpath(value)
        return element


def element_exist(driver, location, value, *args):
    try:
        if location == appium_id:
            get_element(driver, location, value)
            return True

        elif location == appium_ids:
            get_element(driver, location, value, args)
            return True

        elif location == appium_name:
            get_element(driver, location, value)
            return True

        elif location == appium_nameLike:
            get_element(driver, location, value)
            return True

        elif location == appium_className:
            get_element(driver, location, value)
            return True

        elif location == appium_accessibility:
            get_element(driver, location, value)
            return True

        elif location == appium_xpath:
            get_element(driver, location, value)
            return True
    except NoSuchElementException:
        # print 'No such element found.'
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
    if locate(dr).zhanghao_find_by_id:
        return True
    else:
        return False


def logout():
    dr = used_driver()
    # dr = get_driver()
    locate(dr).zhanghao_find_by_id.click()
    # swipe two times
    swipe_up()
    swipe_up()
    time.sleep(1)
    locate(dr).shezhi_find_by_name.click()
    time.sleep(1)
    dr.find_element_by_id('com.talk51.dasheng:id/setting_logout').click()
    dr.find_element_by_id('com.talk51.dasheng:id/button1').click()
    time.sleep(2)


def if_cpad():  # 插屏广告判断
    dr = used_driver()
    if if_element_exist('by_id', 'com.talk51.dasheng:id/img'):
        dr.find_element_by_id('com.talk51.dasheng:id/cancel').click()
        time.sleep(1)


def if_ydpage():  # 引导页判断
    dr = used_driver()
    if if_element_exist('by_id', 'com.talk51.dasheng:id/btn_know'):
        dr.find_element_by_id('com.talk51.dasheng:id/btn_know').click()


def if_hongbao():  # 红包弹窗判断
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


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    # print 'width is :', x, 'height is:', y
    # width = 1080, height = 1794
    return x, y


# 向上滑
def swipe_up(driver):
    s = get_size(driver)
    x1 = int(s[0] * 0.5)
    y1 = int(s[1] * 0.5)
    y2 = y1 - y1 * 0.75
    driver.swipe(x1, y1, x1, y2)


# 向下滑
def swipe_down():
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
    all_name = r'E:\wangping\app\src\result\result_' + now + '_' + name + '.png'
    dr.get_screenshot_as_file(all_name)

# 0、此方法失败，直接使用ImageGrab截图，作用的是pc，而不是手机。
# 1、由此需要多一步操作，将手机的图先截取到pc，再使用此方法
# 2、有一点很重要，python自带截手机全图，到pc时分辨率一致。
# 3、然后在全图中截取需要的element大小图片。
def patial_screenshot(ele, bigScreen_pic, smallScreen_pic):
    # 传入需要截取图片位置的4个坐标点；
    # 如果是其他手机来执行测试，尝试使用 (x1/loac_x)*目标机器的分别率进行兼容。
    # adb shell wm size
    # loc_x = 1080
    # loc_y = 1920
    # test_x = driver.get_window_size()['width']
    # test_y = driver.get_window_size()['height']
    # x1 = (x1 / loc_x)*test_x
    # y1 = (y1 / loc_y)*test_y
    # x2 = (x2 / loc_x)*test_x
    # y2 = (y2 / loc_y)*test_y
    # bbox = (x1, y1, x2, y2)
    ima = Image.open("screenshot"+"\\" + bigScreen_pic + ".png")
    coord = ele.location  # 获取控件坐标，是一个tuple
    ele_start_x = int(coord['x'])
    ele_start_y = int(coord['y'])
    ele_end_x = int(ele_start_x) + int(ele.size['width'])
    ele_end_y = int(ele_start_y) + int(ele.size['height'])
    # 上面已经准好定义唯一位置的坐标
    # 下面开始加载截取的图片，并按照以上给定坐标截取空间图片
    newimage = ima.crop((ele_start_x, ele_start_y, ele_end_x, ele_end_y))
    newimage.save("screenshot" + "\\" + smallScreen_pic + ".png")



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
def s2b(string):
    l = []
    for c in string:
        b = bin(ord(c)).replace('0b', '')
        l.append(b)
    print l


# 2进制转字符串, 参数为list
def b2s(binary_list):
    l = []
    for b in binary_list:
        s = chr(int(b, base=2))
        l.append(s)
    print ''.join(l)


def hist_compare(img1_read, img2_read, size=(256, 256)):
    """
    直方图判断两张图片的是否相似的方法就是，计算其直方图的重合程度即可。
    :param img1: 截取的图片名称1
    :param img2: 截取的图片名称1
    :param size: 默认参数
    :return: 相似度，约靠近1约相似 
    这个方法不如下面的方法。
    使用说明：单独使用该方法，可以打开下面的注释。若split_hist_compare调用，需要注掉。
    """
    # 图片缩放
    # 如下，为什么不直接使用注掉的内容，感觉cv2.imread并不能很好的接受参数，并组成路径去寻找图片。
    # img1_read = cv2.imread('..\screenshot' + '\\' + img1 + '.png')
    # path1 = os.path.abspath('.\screenshot' + '\\')
    # path1 = path1 + '\\' + img1 + '.png'
    # # print path1
    # img1_read = cv2.imread(img1)

    # # img2_read = cv2.imread('..\screenshot' + '\\' + img2 + '.png')
    # path2 = os.path.abspath('.\screenshot' + '\\')
    # path2 = path2 + '\\' + img2 + '.png'
    # # print path2
    # img2_read = cv2.imread(img2)

    if img1_read is None or img2_read is None:
        return
    img1_size = cv2.resize(img1_read, size)
    img2_size = cv2.resize(img2_read, size)
    # 转化为直方图的输入数据列表
    img1_hist = cv2.calcHist([img1_size], [0], None, [256], [0.00, 256.00])
    img2_hist = cv2.calcHist([img2_size], [0], None, [256], [0.00, 256.00])
    # 使用matplotlib库绘图,使展示在同一界面可进行比较
    pyplot.plot(range(256), img1_hist, 'r')
    pyplot.plot(range(256), img2_hist, 'b')
    # pyplot.show()
    # 计算直方图的重合程度
    degree = 0
    for i in range(len(img1_hist)):
        if img1_hist[i] != img2_hist[i]:
            degree = degree + (1 - abs(img1_hist[i] - img2_hist[i]) / max(img1_hist[i], img2_hist[i]))
        else:
            degree = degree + 1
    degree = degree / len(img1_hist)
    return degree


def split_hist_compare(img1, img2, size=(256, 256)):
    # 分离为三个单独的通道，计算平均值；上面是求三通道的相似值
    path1 = os.path.abspath('..\screenshot' + '\\')
    path1 = path1 + '\\' + img1 + '.png'
    print path1
    img1_read = cv2.imread(path1)

    # img2_read = cv2.imread('..\screenshot' + '\\' + img2 + '.png')
    path2 = os.path.abspath('..\screenshot' + '\\')
    path2 = path2 + '\\' + img2 + '.png'
    print path2
    img2_read = cv2.imread(path2)

    if img1_read is None or img2_read is None:
        return

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
    """
    # 此算法是基于比较灰度图每个像素与平均值来实现的
    1.缩放图片，一般大小为8*8，64个像素值。
    2.转化为灰度图
    3.计算平均值：计算进行灰度处理后图片的所有像素点的平均值，直接用numpy中的mean()计算即可。
    4.比较像素灰度值：遍历灰度图片每一个像素，如果大于平均值记录为1，否则为0.
    5.得到信息指纹：组合64个bit位，顺序随意保持一致性。
    6.比对两张图片的指纹，获得汉明距离即可。
    """
    path1 = os.path.abspath('.\screenshot' + '\\')
    path1 = path1 + '\\' + image1 + '.png'
    print path1
    img1_read = cv2.imread(path1)

    # img2_read = cv2.imread('..\screenshot' + '\\' + img2 + '.png')
    path2 = os.path.abspath('.\screenshot' + '\\')
    path2 = path2 + '\\' + image2 + '.png'
    print path2
    img2_read = cv2.imread(path2)

    if img1_read is None or img2_read is None:
        return
    image1 = cv2.resize(img1_read, (8, 8))
    image2 = cv2.resize(img2_read, (8, 8))
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    hash1 = getHash(gray1)
    hash2 = getHash(gray2)
    return hanming_distance(hash1, hash2)


# p 哈希算法
def classify_pHash(image1, image2):
    """
    平均哈希算法过于严格，不够精确，更适合搜索缩略图，为了获得更精确的结果可以选择[感知哈希算法]，
    它采用的是DCT（离散余弦变换）来降低频率的方法

    一般步骤：
    
    1、缩小图片：32 * 32是一个较好的大小，这样方便DCT计算
    2、转化为灰度图
    3、计算DCT：利用Opencv中提供的dct()方法，注意输入的图像必须是32位浮点型，所以先利用numpy中的float32进行转换
    4、缩小DCT：DCT计算后的矩阵是32 * 32，保留左上角的8 * 8，这些代表的图片的最低频率
    5、计算平均值：计算缩小DCT后的所有像素点的平均值。
    6、进一步减小DCT：大于平均值记录为1，反之记录为0.
    7、得到信息指纹：组合64个信息位，顺序随意保持一致性。
    8、最后比对两张图片的指纹，获得汉明距离即可。
    """
    path1 = os.path.abspath('.\screenshot' + '\\')
    path1 = path1 + '\\' + image1 + '.png'
    print path1
    img1_read = cv2.imread(path1)

    # img2_read = cv2.imread('..\screenshot' + '\\' + img2 + '.png')
    path2 = os.path.abspath('.\screenshot' + '\\')
    path2 = path2 + '\\' + image2 + '.png'
    print path2
    img2_read = cv2.imread(path2)

    if img1_read is None or img2_read is None:
        return
    image1 = cv2.resize(img1_read, (32, 32))
    image2 = cv2.resize(img2_read, (32, 32))
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
    # 汉明距离越小，则代表相似度越高。汉明距离为0，即代表两张图片完全一样
    hm_value = 0
    for hm_index in range(len(bin_list1)):
        if bin_list1[hm_index] != bin_list2[hm_index]:
            hm_value = hm_value + 1
    return u'总位数为{}, 有{}位不同'.format(len(bin_list1), hm_value)  # 总位数，以及相异位数

# 修改课程时，判断青少or成人，然后修改青少或者成人的课程
def get_nameOfLessonType(driver):
    name = u'经典英语青少'
    try:
        if element_exist(driver, appium_nameLike, name):
            return name
        else:
            name = u'经典英语'
            return name
    except NoSuchElementException:
        pass

def my_logging():
    # 设置默认的level为DEBUG
    # 设置log的格式
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s"
    )

if __name__ == '__main__':
    result = classify_aHash('price_smallPic1', 'price_smallPic2')
    print result

