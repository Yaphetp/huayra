import unittest
import time

class myDemo():


    def mytest_01(self):
        self.a= 1
        print 'it`s mytest01 the value is {}'.format(self.a)
        time.sleep(1)


    def mytest_02(self):
        print 'it`s mytest02 the value is {}'.format(self.a)
        time.sleep(1)


    def mytest_03(self):
        print 'it`s mytest03 the value is {}'.format(self.a)
        time.sleep(1)

mydemo= myDemo()
mydemo.mytest_01()
mydemo.mytest_02()
mydemo.mytest_03()
