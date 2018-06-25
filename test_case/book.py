# coding=utf-8
# encoding = utf-8

import time
import unittest
# from common.appiumDriver import used_driver
from common.appiumDriver import get_driver
from common.commons import defined_tap, random_tap, if_is_booked
from selenium.common.exceptions import NoSuchElementException
from common.commons import swipe_up, swipe_left, swipe_down
from cancel_book import BookCancel
from common import variable
from common.constant import locate
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')  # 小班课约课使用，部分中文字段截取


class Book(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.dr = used_driver()
        cls.dr = get_driver()

    def test_single_book(self):
        try:
            locate(self.dr).yueke_find_by_id.click()
            time.sleep(5)
            self.dr.find_element_by_id('com.talk51.dasheng:id/rl_seach_time').click()
            time.sleep(2)
            defined_tap(540, 480, 1080, 1920)
            defined_tap(540, 917, 1080, 1920)
            self.dr.find_element_by_id('com.talk51.dasheng:id/save_date_time').click()
            time.sleep(2)
            self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_bookClass_yuyue')[2].click()
            time.sleep(1)
            self.dr.find_element_by_id('com.talk51.dasheng:id/goAhead').click()

            if_is_booked()
            self.dr.find_element_by_id('com.talk51.dasheng:id/tv_left').click()
            # 去首页，取消所有课程

            self.assertEqual(self.dr.find_element_by_id('com.talk51.dasheng:id/tv_title').text, u'约课成功', u'约课未成功')
            time.sleep(5)
            self.dr.find_element_by_id('com.talk51.dasheng:id/tv_left').click()
            time.sleep(1)
        except NoSuchElementException, e:
            print e

    def test_batch_book(self):
        yueke_find_by_id.click()
        time.sleep(5)
        self.dr.find_element_by_id('com.talk51.dasheng:id/rl_seach_time').click()
        time.sleep(2)
        defined_tap(540, 480, 1080, 1920)
        defined_tap(540, 917, 1080, 1920)
        self.dr.find_element_by_id('com.talk51.dasheng:id/save_date_time').click()
        time.sleep(2)
        for list_index in range(5):
            self.dr.find_elements_by_id('com.talk51.dasheng:id/ll_tea')[list_index].click()
            time.sleep(1)
            self.dr.find_element_by_id('com.talk51.dasheng:id/tv_appoint').click()
            time.sleep(1)
            # 错误代码示例
            # self.dr.find_element_by_id(id_name).text in id_text = self.assertEqual(
            #     self.dr.find_element_by_id('com.talk51.dasheng:id/tv_selected_classnum').text, u'您已选择 2 节课')
            # self.dr.find_element_by_id(id_name).text not in id_text = self.assertNotEqual(
            #     self.dr.find_element_by_id('com.talk51.dasheng:id/tv_selected_classnum').text, u'您已选择 2 节课')
            id_name = 'com.talk51.dasheng:id/tv_selected_classnum'
            id_text = [u'您已选择 2 节课', u'您已选择 3 节课']

            # 当前区域
            for i in range(2):
                random_tap(320, 960, 480, 1600, 1080, 1920)
                if self.dr.find_element_by_id(id_name).text in id_text:
                    break
            # 下方区域
            if self.dr.find_element_by_id(id_name).text not in id_text:
                i = 0
                while self.dr.find_element_by_id(id_name).text not in id_text and i <= 2:
                    swipe_up()
                    swipe_up()
                    for j in range(2):
                        random_tap(320, 960, 480, 1600, 1080, 1920)
                        if self.dr.find_element_by_id(id_name).text in id_text:
                            print 'is chosen'
                            break
                    if self.dr.find_element_by_id(id_name).text in id_text:
                        break
                    i = i + 1
            # 中间区域
            if self.dr.find_element_by_id(id_name).text not in id_text:
                for t in range(4):
                    swipe_left()
                for j in range(5):
                    random_tap(320, 960, 480, 1600, 1080, 1920)
                    if self.dr.find_element_by_id(id_name).text in id_text:
                        break
                i = 0
                while self.dr.find_element_by_id(id_name).text not in id_text and i <= 2:
                    swipe_down()
                    swipe_down()
                    for j in range(5):
                        random_tap(320, 960, 480, 1600, 1080, 1920)
                        if self.dr.find_element_by_id(id_name).text in id_text:
                            break
                    if self.dr.find_element_by_id(id_name).text in id_text:
                        break
                    i = i + 1

            # 右侧区域
            if self.dr.find_element_by_id(id_name).text not in id_text:
                for t in range(4):
                    swipe_left()
                for j in range(5):
                    random_tap(320, 960, 480, 1600, 1080, 1920)
                    if self.dr.find_element_by_id(id_name).text in id_text:
                        break
                i = 0
                while self.dr.find_element_by_id(id_name).text not in id_text and i <= 2:
                    swipe_up()
                    swipe_up()
                    for j in range(5):
                        random_tap(320, 960, 480, 1600, 1080, 1920)
                        if self.dr.find_element_by_id(id_name).text in id_text:
                            break
                    if self.dr.find_element_by_id(id_name).text in id_text:
                        break
                    i = i + 1

            # 如果依然未选中，退出约课界面，选择下一个老师
            if self.dr.find_element_by_id(id_name).text not in id_text:
                self.dr.find_element_by_id('com.talk51.dasheng:id/iv_back').click()
                self.dr.find_element_by_id('com.talk51.dasheng:id/iv_back').click()

            try:
                if self.dr.find_element_by_id(id_name).text in id_text:
                    self.dr.find_element_by_id('com.talk51.dasheng:id/tv_sure_order').click()
                    self.dr.find_element_by_id('com.talk51.dasheng:id/goAhead').click()
                    time.sleep(2)
                    self.assertEqual(self.dr.find_element_by_id('com.talk51.dasheng:id/tv_title').text, u'约课成功',
                                     u'约课未成功')
                    time.sleep(2)
                    self.dr.find_element_by_id('com.talk51.dasheng:id/tv_left').click()
                    break
            except NoSuchElementException, e:
                print e

    def test_mini_class_book(self):
        locate(self.dr).yueke_find_by_id.click()
        self.dr.find_element_by_name('小班课').click()
        print 'start'
        print self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_time')[0].text[:6]
        while True in map(
                lambda x: self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_time')[x].text[:6]\
                        == variable.mini_class_date, [0, 1]):
            swipe_up()
            swipe_up()
            time.sleep(1)

            # 如果发生第二天的第一节课被【已预约】，则需要继续向下滑动；直到出现【预约】
        while self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_reserv')[1].text == u'已预约':
            swipe_up(); swipe_up()
            if self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_reserv')[1].text == u'预约':
                break
        self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_reserv')[1].click()
        time.sleep(5)
        self.assertEqual(self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_reserv')[1].text,\
                         u'已预约', u'小班课预约失败')


def book():
    suit = unittest.TestSuite()
    # suit.addTest(Book('test_single_book'))
    # suit.addTest(BookCancel('cancel_1v1class_book'))
    # suit.addTest(Book('test_batch_book'))
    # suit.addTest(BookCancel('cancel_1v1class_book'))
    suit.addTest(Book('test_mini_class_book'))
    suit.addTest(BookCancel('cancel_miniclass_book'))
    return suit
