# coding = utf-8
# encoding:utf-8

import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  # 小班课约课使用，部分中文字段截取

# get date(today), for mini_class_book
mini_class_date = time.strftime('%m月%d日', time.localtime(time.time()))

t_name = ['hanmeimei', 'Jacleen', 'Jake']