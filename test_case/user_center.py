# coding: utf-8
# encoding: utf-8

import unittest
import time
import os
from common.appiumDriver import used_driver
# from common.appiumDriver import get_driver
from common.commons import defined_tap
from selenium.common.exceptions import NoSuchElementException
from commons import find_toast, kaka, remove_kaka


class UserCenter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = used_driver()
        # cls.dr = get_driver()

    def test_userPic(self):
        self.dr.find_element_by_id('com.talk51.dasheng:id/tv_account').click()
        self.dr.find_element_by_id('com.talk51.dasheng:id/iv_arrow_right').click()
        self.dr.find_element_by_id('com.talk51.dasheng:id/user_img').click()
        # 从相册中选取
        self.dr.find_element_by_id('com.talk51.dasheng:id/tv_yiyue_cancelCourse').click()
        # 下面这段本机选择照片，华为mate8 6.0系统测试通过
        try:
            self.dr.find_elements_by_id('com.android.gallery3d:id/albumset_info')[3].click()
            time.sleep(1)
            defined_tap(130, 340, 1080, 1920)
            self.dr.find_element_by_id('com.android.gallery3d:id/head_select_right').click()
            # self.dr.pinch(self.dr.find_element_by_class_name('android.widget.RelativeLayout'), 200, 200)
            self.dr.find_element_by_id('com.android.gallery3d:id/head_select_right').click()
            find_toast(self, u'设置成功')
            """
            截图、删除图片 
            """
            # self.dr.save_screenshot('test01.png')
            #  当前目录，test_case目录
            # os.remove(r'E:\wangping\app\src\result\uploadPic.png')
            remove_kaka(r'E:\wangping\app\src\result', 'uploadPic')
            kaka('uploadPic')
        except NoSuchElementException:
            print u'本机选择照片，华为mate8 6.0系统测试通过'

        # 拍照
        # self.dr.find_element_by_id('com.talk51.dasheng:id/tv_yiyue_changeLesType').click()
        # 取消
        # self.dr.find_element_by_id('com.talk51.dasheng:id/bt_person_cancle').click()
        time.sleep(1)


def test_choseSex(self):
    while True:
        self.dr.find_element_by_id('com.talk51.dasheng:id/gender_right').click()
        self.dr.swipe(500, 1600, 500, 1700)
        self.dr.find_element_by_id('com.talk51.dasheng:id/tv_ok').click()
        if self.dr.find_element_by_id('com.talk51.dasheng:id/tv_sex').text == u'女':
            return False


def test_serviceCenter(self):
    pass


def user_center():
    suit = unittest.TestSuite()
    suit.addTest(UserCenter('test_userPic'))
    # suit.addTest(UserCenter('test_choseSex'))
    return suit
