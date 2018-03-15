# coding=utf-8
import unittest


from test01 import Test1704


class Test1705(unittest.TestCase):
    def setUp(self):
        self.b = 2

    def test002(self):
        print 'excute test002'
        print self.b


def suit02():
    suit = unittest.TestSuite()
    suit.addTest(Test1704('test001'))
    suit.addTest(Test1705('test002'))
    runner = unittest.TextTestRunner()
    runner.run(suit)

suit02()