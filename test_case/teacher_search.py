# coding: utf-8
# encoding: utf-8
import sys
import time
import unittest
from common.appiumDriver import used_driver
# from common.appiumDriver import get_driver
from common.commons import defined_tap
from constant import button_1v1_yueke
from variable import t_name
from selenium.common.exceptions import NoSuchElementException


class SearchTeacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = used_driver()
        # cls.dr = get_driver()

    def test_search_1v1teacher(self):
        time.sleep(2)
        self.dr.find_element_by_id(button_1v1_yueke).click()
        self.dr.find_element_by_id('com.talk51.dasheng:id/tv_filter').click()
        self.dr.find_element_by_id('com.talk51.dasheng:id/edittxt_tea_name').click()
        for name in t_name:
            self.dr.find_element_by_id('com.talk51.dasheng:id/edittxt_tea_name').send_keys(name)
            time.sleep(1)
            self.dr.keyevent(66)
            self.dr.press_keycode(66)
            try:
                if self.dr.find_element_by_id('com.talk51.dasheng:id/tv_seateacher_name').text == name:
                    break

            except NoSuchElementException:
                print 'can`t find this techer`s name'
                # self.assertEqual(self.dr.find_element_by_id('com.talk51.dasheng:id/tv_seateacher_name').text, 'Jacleen', 'Not Find')

    def test_1v1_teaShare(self):
        defined_tap(550, 500, 1080, 1920)
        self.dr.find_element_by_id('com.talk51.dasheng:id/image_share').click()
        defined_tap(170, 1730, 1080, 1920)
        self.dr.find_element_by_id('com.tencent.mm:id/arp').click()
        self.dr.hide_keyboard()
        self.dr.find_element_by_id('com.tencent.mm:id/arp').send_keys(u'牧羊王')
        self.assertEqual(self.dr.find_element_by_id('com.tencent.mm:id/kh').text, u'牧羊王', 'Not find the contact')
        self.dr.find_element_by_id('com.tencent.mm:id/kh').click()
        self.dr.find_element_by_id('com.tencent.mm:id/alo').click()
        self.dr.find_element_by_id('com.tencent.mm:id/aln').click()


def search_teacher():
    suit = unittest.TestSuite()
    suit.addTest(SearchTeacher('test_search_1v1teacher'))
    suit.addTest(SearchTeacher('test_1v1_teaShare'))
    return suit
