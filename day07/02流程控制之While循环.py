#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DailyCode 
@File    ：02流程控制之While循环.py
@IDE     ：PyCharm 
@Author  ：wangyuqi
@Date    ：2021/6/30 6:52 下午 
'''

"""
while 条件:
    代码1
    代码2
    代码3
"""
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# print("顶级代码")
#
#
# 2、循环应用

username ='wangyuqi'
password = 'wangyuqi1'
tag =True

# while tag:
#     inp_name = input("请输入您的帐号")
#     inp_pwd = input("请输入您的密码")
#
#     if inp_name == username and inp_pwd == password :
#         print("输入正确")
#         tag = False
#     else:
#         print("输入错误")
#     print("循环结束")

# 方式二 break ，只要运行到break就会立刻终止本层循环

# while True:
#     inp_name = input("请输入您的帐号")
#     inp_pwd = input("请输入您的密码")
#
#     if inp_name == username and inp_pwd == password :
#         print("输入正确")
#         while True:
#             cmd = input("请输入命令")
#             if cmd == 'q':
#                 break
#         print("命令{x}正在执行".format(x=cmd))
#         break
#     else:
#         print("输入错误")
#     print("循环结束")



#  8、while + continue : 结束本次循环，直接进入下一次
# 在 continue 之后添加同级代码毫无意义，永远无法运行
count = 0
while count < 6:
    if count == 4:
        count += 1
        continue
    print(count)
    count+=1





