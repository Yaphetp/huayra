# coding:utf-8

import unittest
from common.appiumDriver import used_driver
# from common.appiumDriver import get_driver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from common.commons import swipe_up, CancelBookError
from common.constant import locate
import time


# from commons import find_toast


class BookCancel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.dr = get_driver()
        cls.dr = used_driver()

    def cancel_1v1class_book(self):
        locate(self.dr).shouye_find_by_Id.click()
        try:
            while self.dr.find_element_by_id('com.talk51.dasheng:id/btn_enter_class').text == u'预习':
                # if self.dr.find_elements_by_id('com.talk51.dasheng:id/tv_course_date')[0].text[:10] == u'12月07日':
                self.dr.tap([(400, 500)])
                time.sleep(1)
                swipe_up()
                self.dr.find_element_by_id('com.talk51.dasheng:id/btn_cannel').click()
                self.dr.find_element_by_id('com.talk51.dasheng:id/button1').click()
                # find_toast(u'取消成功')
        except NoSuchElementException, ne:
            print ne
        except CancelBookError:
            print u'无可取消课程'

    def cancel_miniclass_book(self):
        locate(self.dr).shouye_find_by_Id.click()
        try:
            while self.dr.find_element_by_id('com.talk51.dasheng:id/tv_class_type').text == u'小班课':
                self.dr.find_element_by_id('com.talk51.dasheng:id/tv_class_type').click()
                self.dr.tap([(500, 500)])
                WebDriverWait(self.dr, 10).until(lambda x: x.find_element_by_id('com.talk51.dasheng:id/btn_cannel'),\
                                                 'Failed to cancel mini_class_book')
                self.dr.find_element_by_id('com.talk51.dasheng:id/btn_cannel').click()
                self.dr.find_element_by_id('com.talk51.dasheng:id/button1').click()
        except NoSuchElementException:
            print u'未发现其他小班课，所有小班课已取消'


def cb_suit():
    suit = unittest.TestSuite()
    suit.addTest(BookCancel('cancel_1v1class_book'))
    suit.addTest(BookCancel('cancel_miniclass_book'))
    return suit
