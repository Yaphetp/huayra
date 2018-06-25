# coding:utf-8
import time
import unittest
# from common.appiumDriver import used_driver
from common.commons import if_unlogin, login, if_cpad, if_ydpage, if_hongbao, logout


class TestLogin(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.dr = used_driver()

    def test_login(self):
        """
        1、判断是否未登录，若未登录，执行登录；
        2、若已登录，则退出登录（首先关闭各种弹窗），重新登录
        """
        if if_unlogin():
            login()
        else:
            self.test_otherPage()
            logout()
            login()
            time.sleep(8)

    def test_otherPage(self):
        if_cpad()
        if_ydpage()
        if_hongbao()

    def test_logout(self):
        logout()


def login_suit():
    suit = unittest.TestSuite()
    suit.addTest(TestLogin('test_login'))
    suit.addTest(TestLogin('test_otherPage'))
    # 有必要的时候再使用logout
    # suit.addTest(TestLogin('test_logout'))
    return suit
