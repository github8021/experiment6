# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment6
# @File     :text1
# @Date     :2020/10/4 21:40
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
contacts = {"姓名":"电话"}
while (True):
    print("""
-------------------------------------------------
==============通讯录管理系统==================
1.增加姓名和手机
2.删除姓名
3.修改手机
4.查询所有用户
5.根据姓名查找手机号
6.退出
-------------------------------------------------
    """)
    i = int(input("请根据规则继续输入：>"))
    if (i == 1):
        name=str(input("请输入姓名：>"))
        phone=str(input("请输入手机号：>"))
        contacts[name]=phone
        print("添加完成")
    elif (i == 2):
        name=str(input("请输入要删除的联系人：>"))
        contacts.pop(name)
        print("此联系人已经删除！！")
    elif (i == 3):
        name = str(input("请输入要修改的联系人：>"))
        phone = str(input("请输入要修改的电话号码：>"))
        contacts[name] = phone
        print("手机号码修改成功！")
    elif (i == 4):
        print("--------------------------------")
        for item in contacts:
            print(item,contacts.get(item))
        print("--------------------------------")
    elif (i == 5):
        name = str(input("请输入要查询的联系人：>"))
        print(contacts.get(name))
    elif (i == 6):
        print("您已成功退出")
        exit()