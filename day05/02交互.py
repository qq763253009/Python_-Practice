#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DailyCode 
@File    ：02交互.py
@IDE     ：PyCharm 
@Author  ：wangyuqi
@Date    ：2021/6/20 1:50 下午 
'''

# input_username= input("请输入")
# print(input_username,type(input_username))
# x = int(input_username)
# print(x>17)

"""
格式化输出 %s
"""
res = "my name is %s,and age %s" %("wyq","22")
print(res)

# 以字典的形式传值，打破位置的限制
res1 = "我的名字是：%(name)s,and 我的年龄是: %(age)s" %{"name":"王钰琪","age":"18"}
print(res1)


# str.format

print(res)


res = f'{10+3}'
print(res)

res = '10+3'
print(res)