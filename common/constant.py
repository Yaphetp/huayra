# coding=utf-8

import time

def locate(dr, ids, names,className):
    '''
    里面通过条件筛选，使用不同的定位方法
    '''
    shouye_find_by_id = dr.find_element_by_id(id_a)
    yueke_find_by_id = dr.find_element_by_id('com.talk51.dasheng:id/tv_bespoke')
    # 这里是定义，不能使用实际值
    # zhanghao_find_by_id = dr.find_element_by_id('com.talk51.dasheng:id/tv_account')
    # shezhi_find_by_name = dr.find_element_by_android_uiautomator('text(\"设置\")')

    return shouye_find_by_id


screenshot_url = r'E:\wangping\git-github01\result'
now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
