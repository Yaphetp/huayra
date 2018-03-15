# coding: utf-8
import unittest
import time
import HTMLTestRunner

class Atest(unittest.TestCase):
    def setUp(self):
        self.a = 1

    def test_04(self):
        print 'it`s mytest04 the value is {}'.format(self.a)
        time.sleep(1)

    def test_05(self):
        print 'it`s mytest05 the value is {}'.format(self.a)
        time.sleep(1)

    def test_06(self):
        print 'it`s mytest06 the value is {}'.format(self.a)
        time.sleep(1)


if __name__ == '__main__':
    suits = unittest.TestSuite()
    # suits.addTests(map(Test, ['test_04', 'test_05', 'test_06']))
    suits.addTest(Atest('test_04'))
    suits.addTest(Atest('test_05'))
    suits.addTests(map(Atest, ['test_04', 'test_05']))
    suits.addTest(unittest.makeSuite(Atest))
    suitsss = unittest.TestSuite([suits, suitss])
    suit1 = unittest.TestLoader().loadTestsFromTestCase(Atest)

    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))




    runner = unittest.TextTestRunner()
    runner.run(suit1)