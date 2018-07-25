# -*- coding: utf-8 -*-
"""
第一步：准备存储课程购买相关页面的定位值等。
"""
from appium import webdriver

dedress_id = 'com.talk51.kid:id/alertTitle'

dedress_name = u'完善收货地址'  # 完善收货地址弹框

xczs_id = 'com.talk51.kid:id/button2'  # 下次再说button

tx_id = 'com.talk51.kid:id/button1'  # 填写button

gmkc_id = 'com.talk51.kid:id/rl_buy'  # 购买课程button

qhxx_xpath = "//*[@id='app']/div/ul/li[1]"  # 强化学习效果套餐

tcxl_xpath ='//*[@id="app"]/div/div[3]/span'  # 套餐下拉

tcxz_xpath ='//*[@id="app"]/div/div[7]/div/div/ul/li[2]/p'  #套餐选择

qrbt_xpath ='//*[@id="app"]/div/div[7]/div/div/div/button'  #确认按钮

price1_xpath ='//*[@id="app"]/div/div[7]/div/div/div/div/div[2]'  # 弹窗页面价格显示

price2_xpath = '//*[@id="app"]/div/div[2]/div[1]/div[1]/p[3]'  # 选择套餐后，主页面价格显示

qrgm_xpath ='//*[@id="app"]/div/div[5]/button'  # 确认购买button

fwxy_xpath ='//*[@id="app"]/div/div/div[2]'  # 同意51Talk课程服务协议






