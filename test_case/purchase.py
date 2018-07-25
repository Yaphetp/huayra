# -*- coding: utf-8 -*-

import unittest
import time
from appiumDriver import get_driver
from common.commons import if_element_exist, get_element, appium_id, \
    appium_name,appium_xpath ,appium_accessibility, patial_screenshot, remove_kaka, \
    hist_compare, split_hist_compare, classify_aHash, classify_pHash
from po.purchase_page import *
from common.common_elements import zh_value
import base64
from selenium.common.exceptions import NoSuchElementException
from PIL import Image
import os


class Purchase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 所有用例（方法）运行前，运行1次
        cls.dr = get_driver()
        # cls.dr.implicitly_wait()

    @classmethod
    def tearDownClass(cls):  # # 所有用例（方法）运行后，运行1次
        cls.dr.quit()

    def test_purchase(self):
        '''
        购买课程
        '''
        ele = get_element(self.dr, appium_id, zh_value)
        ele.click()

        if if_element_exist(self.dr, appium_name, dedress_name):
            ele = get_element(self.dr, appium_id, xczs_id)
            ele.click()

        ele = get_element(self.dr, appium_id, gmkc_id)  # 点击‘购买课程’按钮
        ele.click()
        time.sleep(3)
        print self.dr.contexts
        self.dr.switch_to.context('WEBVIEW_com.talk51.kid')
        ele = get_element(self.dr, appium_xpath, qhxx_xpath)
        ele.click()  # 点击强化套餐，进入详情页
        time.sleep(2)
        ele = get_element(self.dr, appium_xpath, tcxl_xpath)
        ele.click()  # 点击套餐下拉，进入弹窗选择
        time.sleep(2)
        ele = get_element(self.dr, appium_xpath, tcxz_xpath)
        ele.click()  # 选择第二个套餐
        time.sleep(2)

        # 下面进行截图操作
        # self.dr.switch_to.context('NATIVE_APP')  # 这种方法十分不可取，还是使用webview的截图方法吧
        time.sleep(2)
        remove_kaka('\\screenshot', 'price')  # 首先清除之前的历史截图，名称含‘price’的全删。
        # windows下可使用如下写法-- 相对路径
        # 这种写法的相对路径，是从根目录向下找
        img = self.dr.get_screenshot_as_base64()
        imagedata = base64.b64decode(img)
        print(imagedata)
        test_file = open('screenshot\\base64' + '.png', "wb")
        test_file.write(imagedata)
        test_file.close()
        print img
        # self.dr.save_screenshot('screenshot\\price_bigPic1' + '.png')  # 截取第一张大图，直接截全屏
        time.sleep(2)
        print 'the end'

        '''
        ele = get_element(self.dr, appium_accessibility, price1_xpath)  # 截取第1张小图，指定位置截取
        patial_screenshot(ele, "price_bigPic1", "price_smallPic1")
        time.sleep(5)

        # 确认后关闭弹窗，进入购买页面
        ele = get_element(self.dr, appium_xpath, qrbt_xpath)
        ele.click()  # 点击确认按钮

        self.dr.save_screenshot('screenshot\\price_bigPic2' + '.png')  # 截取第二张大图，直接截全屏
        time.sleep(2)

        ele = get_element(self.dr, appium_accessibility, price2_xpath)  # 截取第2张小图，指定位置截取
        patial_screenshot(ele, "price_bigPic2", "price_smallPic2")
        time.sleep(5)

        # 下面进行两张图片比较，smallPic1 vs smallPic2
        # 注意，以下方法中的路径是否正确，..\screenshot\
        # degree = hist_compare('price_smallPic1', 'price_smallPic2')  # 该方s法的相似度仅为0.51354361
        # degree = split_hist_compare('price_smallPic1', 'price_smallPic2')  # 该方法相似度为 0.71872467
        # hanming_distance = classify_aHash('price_smallPic1', 'price_smallPic2')
        #       相传此哈希算法，过于严格，用来搜索缩略图,aHash的结果是(64, 12)
        hanming_distance = classify_pHash('price_smallPic1', 'price_smallPic2')  #pHash的结果是(64, 0)
        print hanming_distance

        ele = get_element(self.dr, appium_accessibility, qrgm_xpath)  # 确认购买按钮
        ele.click()
        time.sleep(5)

        ele = get_element(self.dr, appium_accessibility, fwxy_xpath)  # 服务协议
        ele.click()

        print self.dr.contexts
        time.sleep(5)
        '''

def purchaseSuit():
    suit = unittest.TestSuite()
    suit.addTest(Purchase('test_purchase'))
    return suit

if __name__ == '__main__':
    unittest.main()
