# coding=utf-8
import unittest
import time
from appiumDriver import get_driver
from common.commons import swipe_up, appium_ids, get_element, appium_id, appium_nameLikeIndex, element_exist
from common.commons import get_nameOfLessonType
from po.yueke_page import *
from common.commons import logger


class NewBook(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.implicitly_wait(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_book2end(self):
        '''
        约课至最后一课
        '''

        # 提前预约完成一节课程，入口从这里开始
        # 点击首页
        ele = get_element(self.driver, appium_id, main_page)
        ele.click()

        while True:
            # 进入课程详情页
            ele = get_element(self.driver, appium_ids, course_pic, 0)
            ele.click()

            # 获取教材类型（成人 or 青少）
            lesson_name = get_nameOfLessonType(self.driver)
            # print lesson_name
            logger.info(lesson_name)

            # 成人课程详情页可以不下换，但是青少课程详情页必须下滑
            swipe_up(self.driver)

            # 修改课程教材, 成人与青少同一个元素但属性不同，故需判断
            if element_exist(self.driver, appium_id, change_adult_course):
                ele = get_element(self.driver, appium_id, change_adult_course)
                ele.click()
            else:
                ele = get_element(self.driver, appium_id, change_k12_course)
                ele.click()

            # 主修课, 专业课和选修课不需要，因为这俩种课程直接可以预约到最后一课。
            ele = get_element(self.driver, appium_ids, kcxz_next, 0)
            ele.click()

            ele = get_element(self.driver, appium_nameLikeIndex, lesson_name, 0)
            ele.click()

            ele = get_element(self.driver, appium_ids, unit_choose, 0)  # 第一行的单元
            ele.click()

            ele = get_element(self.driver, appium_ids, checkBox_selected, 0)
            is_selected = ele.is_selected()

            if is_selected is True:
                break
            else:
                ele = get_element(self.driver, appium_ids, book_choose, 0)  # 第一行的课程
                ele.click()

        time.sleep(5)


def book2end():
    suit = unittest.TestSuite()
    suit.addTest(NewBook('test_book2end'))
    return suit


if __name__ == '__main__':
    unittest.main()
