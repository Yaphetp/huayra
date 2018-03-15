# !/usr/bin/python
# coding=utf-8


import re
import os
from commons import remove_kaka, s2b, b2s
from numpy import *
import binascii
import chardet
import cv2
import numpy as np
import sys
from matplotlib import pyplot
from commons import hist_compare
from commons import split_hist_compare, hanming_distance
"""
from __future__ import division

class DivisionException(Exception):
      def __init__(self, x, y):
            Exception.__init__ (self, x, y)       
            self.x = x
            self.y = y
if __name__ == "__main__":
    try:
        x = 3
        y = 2
        if x % y > 0 :                               
            print 'x / y = ', x/y
            raise DivisionException(x,y)
    except DivisionException, z:                     
        print "DivisionExcetion: x/y = %.2f" % (z.x/z.y)
"""

# i = 0
# j = 1
# while i != 2 and j < 20:
#     print 'start time', j
#     if j / 2 == 5:
#         i = 2
#     else:
#         i = 0
#         j = j + 1
# print lambda x, y: x + y (1,2)
'''
def f1():
    print(1/0)

def f2():
    try:
        f1()
    except Exception as e:
        e.args += ('more info',)
        raise # don't raise e !!!

f2()
while True in map(lambda x: x == 1, [3, 2]):
    print 'That`s True'
    break

import sys
reload(sys) # Python2.5 初始化后删除了 sys.setdefaultencoding 方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
age =18

print age, age, age, age; print age, age, age, age; print 'Finished test'

a = [1,2,3,4]
l = []
i = 0
# while循环break
while i < 4:
    if a[i] == 3:
        print 'find'
        i = 3
        continue
    else:
        l.append(a[i])
        i += 1
    print l
# for循环break
a = [1, 2, 3, 4, 5]
l = []
for i in a:
    if i == 3:
        continue
    elif i == 5:
        break
    else:
        l.append(i)
print l
list01 = range(10)
list02 = range(5)
list03 = list01 + list02
for i in range(len(list03) - 1, 0, -1):
    for j in range(0, i):
        if list03[j] > list03[j + 1]
            tmp = list03[j + 1]
            list03[j + 1] = list03[j]
            list03[j] = tmp
print list03

# size_str = os.popen('adb shell wm size').read()
# print re.search(r'(\d+)x(\d+)', size_str)
#
key1 = "本机IP123.255.222.107北京市北京市 电信"
key2 = r"<html><body><h1>hello world</h1></body></html>"
key3 ='Doe, John: 555-1212'
key4 = 'Physical size: 1080x1920'
# print re.findall('[12]\d{2}\.[12]\d{2}\.[12]\d{2}\.[12]\d{2}', key1)
# # print re.findall('(\d+{1,3}\.){3}\d+{1,3}\.', key1
# print re.findall('<h([1-6])>.*?</h\1>', key3))
# print re.findall('(?<=<h1>).+(?=</h1>)', key2)
# print re.findall(r'\d+x\d+', key4)
'''

# for root, dirs, files in os.walk(r'E:\wangping\app\src\result', topdown=False):
#     for name in dirs:
#         print (os.path.join(root, name))
#     for name in files:
#         print (os.path.join(root, name))

# def remove_kaka(file_dir, liked_name, *kw):
#     kw = kw
#     for root, dirs, files in os.walk(file_dir, topdown=True):
#         for filename in files:
#             if liked_name in filename and kw == 'file':
#                 os.remove(os.path.join(root, filename))
# print eval('hello')
# 如果使用该

# vector1 = mat([1,1,0,1,0,1,0,0,1])
#
# vector2 = mat([0,1,1,0,0,0,1,1,1])
#
# vector3 = vector1 - vector2
# print vector3 # 得到矩阵 [[1 0 -1 1 0 1 -1 -1 0]]
# cv = nonzero(vector3)
# print cv
# print (shape(cv[0])[1])

# with open(r'C:\Users\wangping\Desktop\a27.jpg', 'rb') as f:
#     f1 = f.read().decode('ascii', 'ignore')
#     print f1
#     print chardet.detect(f1)
#     # print f1.decode('ascii', 'ignore')
#     # print bin(int(binascii.b2a_hex(f1), base=16))
#
# binary_list =['1101000', '1110101', '1100001', '1111001', '1110010', '1100001']
# bs = '110100011101011100001111100111100101100001'
# m = 0
# n = 7
# l = []
# while n <= len(bs):
#     sl = bs[m:n]
#     print sl
#     ss = l.append(sl)
#     m = m + 7
#     n = n + 7
# print l
# img_read = r'C:\Users\wangping\Desktop\spring.png'
# img_size = r'C:\Users\wangping\Desktop\a310.png'
# img1 = cv2.imread(img_read, 1)
# img2 = cv2.imread(img_size, 1)
# (b, g ,r) = cv2.split(img1)
# print img1.shape
# print r.shape
# img_size = cv2.imread(r'C:\Users\wangping\Desktop\a27.jpg', 1)
# print cv2.minMaxLoc(img_hist)
# minval, maxval, minLoc, maxLoc = cv2.minMaxLoc(hist1)
# print np.zeros([5], np.uint8)
# img_shape = np.zeros([256, 256, 3], np.uint8)
# hpt = int (0.9 * 256)

# for h in range(256):
#     intensity = int (img_hist[h] * hpt / maxval)
#     cv2.line(img_shape, (h, 256), (h, 256-intensity), [255, 0, 0])
#
# cv2.imshow('img_shape', img_shape)
# cv2.waitKey(10000)
# cv2.destroyAllWindows()
# print single_hist(img_read, img_size)
# img_read = r'C:\Users\wangping\Desktop\spring.png'
# img_size = r'C:\Users\wangping\Desktop\a310.png'
# img1_read = cv2.imread(img_read, 1)
# img2_read = cv2.imread(img_size, 1)
# image1 = cv2.resize(img1_read,(8,8))
# image2 = cv2.resize(img2_read,(8,8))
# gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)
# # split_hist_compare(img1_read, img2_read)
# ll = []
# for i in range(gray1.shape[0]):
#     for j in range (gray1.shape[1]):
#        print gray1[i ,j]
