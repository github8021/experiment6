# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment6
# @File     :text3
# @Date     :2020/10/4 22:07
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
import random

student = set()

while (True):
    c1 = random.randint(1, 2)
    c2 = random.randint(1, 50)
    c3 = str(c2)
    if(c2<10):
        c3 = "0"+c3
    number="202009"+str(c1)+str(c3)
    student.add(number)
    if(len(student)==20):
        break
for i in student:
    print(i)
