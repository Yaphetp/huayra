# coding= utf-8
from common import serverStartStop
from test_case import login_test, book, cancel_book, teacher_search, user_center
import time
import HTMLTestRunner
from common import appiumDriver
import unittest
from constant import now


# Start Appium
serverStartStop.start_server()
time.sleep(5)
# Start session
appiumDriver.get_driver()

# lg_suit = login_test.login_suit()
# bk_suit = book.book()
# cb_suit = cancel_book.cb_suit()
# ts_suit = teacher_search.search_teacher()
uc_suit = user_center.user_center()

# lg_suit, bk_suit

suits = unittest.TestSuite(uc_suit)      # 将不同的测试套件添加到一个测试套件中
with open(r'E:\wangping\app\src\result\result_' + now + '.html', 'wb')as fp:
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result:', description='result:', verbosity=2)
    runner.run(suits)
