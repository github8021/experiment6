# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment6
# @File     :text2
# @Date     :2020/10/4 22:02
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
urls=['https://www.baidu.com/',
'https://www.ketangpai.com/',
'http://www.gengdan.cn/',
'http://www.gengdan.cn/',
'http://kq.gengdan.cn/',
'https://www.yuque.com/',
'https://www.yuque.com/']
s=set()
for i in urls:
    s.add(i)
print(s)