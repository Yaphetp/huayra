from app_test01 import myDemo
from app_test02 import test

import time

# python/lib
import HTMLTestRunner

import unittest

testsuits = unittest.TestSuite()
testsuits.addTests(map(myDemo,['mytest_01', 'mytest_02', 'mytest_03']))
testsuits.addTests(map(test,['mytest_04', 'mytest_05', 'mytest_06']))
# runner= unittest.TextTestRunner()
now = time.strftime('%Y-%m-%d-%H_%M-%S', time.localtime(time.time()))

with open('result_'+now+'.html', 'wb')as fp:
    # HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result:', description='result:')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result:', description='result:', verbosity=2)
    runner.run(testsuits)