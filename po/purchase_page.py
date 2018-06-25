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

cktc_accessibility = u'强化学习效果套餐'  # 强化学习套餐accessibility定位
qhtc_xpath = "//android.widget.ListView/android.view.View/android.view.View"  # 强化学习套餐xpath， 这个通过chrome打开获取的xpath，未能生效

cktc_xpath = '//*[@id="app"]/div/ul/li[2]'  # 次卡学习套餐xpath， 这个通过chrome打开获取的xpath，未能生效

tc1_accessibility = u'360次次卡+50节优选公开课课时'  # 套餐下拉，套餐会变, 需要维护用例或者使用其他定位。
# tc3_accessibility = u'270次次卡+40节优选公开课课时' # 选择第3个套餐
# tczj_accessibility = u'总价:¥12688'  # 第三个套餐的值
tczj_accessibility = u'总价:¥16488'  # 第1个套餐的值
tcjg_accessibility = u'总价 ¥16488'  # 确认后套餐的价格
qrbt_accessibility = u'确认'  # 确认按钮
qrgm_accessibility = u'确认购买'  # 确认购买

# tcxl_xpath = "//android.webkit.WebView[contains(@content-desc,'购买课程')]/android.view.View[4]"  # 套餐下拉，xpath定位
# tcxl_xpath = "//android.view.View[contains(@content-desc,'已选:')]"

fwxy_accessibility = u'我已阅读并同意51Talk课程服务协议'

//*[@id="app"]/div/ul/li[1]

//*[@id="app"]/div/ul/li[2]/h1


//*[@id="app"]/div/div[3]/span

