# coding=utf-8
import unittest


class Test1704(unittest.TestCase):

    def setUp(self):
        self.b = 1

    def test001(self):
        print 'excute test001.'
        print self.b



def suit01():
    suit =unittest.TestLoader().loadTestsFromTestCase(Test1704)