# -*- coding: utf-8 -*-

import unittest
import time
from appiumDriver import get_driver
from common.commons import if_element_exist, get_element, appium_id, \
    appium_name,appium_xpath ,appium_accessibility, patial_screenshot, remove_kaka, \
    hist_compare, split_hist_compare, classify_aHash, classify_pHash
from po.purchase_page import *
from common.common_elements import zh_value
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

        ele = get_element(self.dr, appium_id, gmkc_id)
        ele.click()
        time.sleep(3)
        print self.dr.contexts  # 获取dirver类型，原生+H5的driver（将H5的driver给下面的值）
        # self.dr.switch_to.context('WEBVIEW_chrome')
        # ele = get_element(self.dr, appium_accessibility, cktc_accessibility)
        # 因为新安装app后，始终打印contexts是native，故无法做上下文的切换，直接使用native的xpath定位，意外之喜竟然成功。
        ele = get_element(self.dr, appium_xpath, qhtc_xpath)  # i can`t belive it.it was sucessful just now
        ele.click()
        print self.dr.contexts
        # 这里使用accessibility不太适用，因为套餐随时可能变化
        # ele = get_element(self.dr, appium_accessibility, tcxl_accessibility)

        # 所以考虑使用xpath定位
        # 因直接使用xpath定位不准，同事说需要从native的driver切换到webview；
        # 但是执行如下代码切换的时候，始终是不成功的，搞了1天半；无果，暂时放弃。
        # print self.dr.contexts  # 获取dirver类型，原生+H5的driver（将H5的driver给下面的值）
        # self.dr.switch_to.context('WEBVIEW_chrome')
        # ele = get_element(self.dr, appium_xpath, gmbt_xpath)
        # 最终还是使用了accessibility_id定位。
        ele = get_element(self.dr, appium_accessibility, tc1_accessibility)
        ele.click()
        time.sleep(2)  # 这个sleep很关键(一点都不关键)，因为弹窗未加载完成需要一段时间。

        # while True:
        #     ele = get_element(self.dr, appium_accessibility, tc3_accessibility)
        #     if not if_element_exist(self.dr, appium_accessibility, tc3_accessibility):
        #         continue
        #     else:
        #         ele.click()
        #         break

        remove_kaka('screenshot', 'price')

        # windows下可使用如下写法-- 相对路径
        # 这种写法的相对路径，是从根目录向下找
        self.dr.save_screenshot('screenshot\\price_bigPic1' + '.png')
        time.sleep(2)

        # 截取第1张图片
        ele = get_element(self.dr, appium_accessibility, tczj_accessibility)
        patial_screenshot(ele, "price_bigPic1", "price_smallPic1")
        time.sleep(5)
        # 确认后关闭弹窗，进入购买页面
        ele = get_element(self.dr, appium_accessibility, qrbt_accessibility)
        ele.click()
        time.sleep(2)

        # 获取全屏截图
        self.dr.save_screenshot('screenshot\\price_bigPic2' + '.png')
        time.sleep(2)

        # 截取第2张图片
        ele = get_element(self.dr, appium_accessibility, tcjg_accessibility)
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

        ele = get_element(self.dr, appium_accessibility, qrgm_accessibility)
        ele.click()

        ele = get_element(self.dr, appium_accessibility, fwxy_accessibility)
        ele.click()
        print self.dr.contexts

        time.sleep(5)


def purchaseSuit():
    suit = unittest.TestSuite()
    suit.addTest(Purchase('test_purchase'))
    return suit

if __name__ == '__main__':
    unittest.main()
