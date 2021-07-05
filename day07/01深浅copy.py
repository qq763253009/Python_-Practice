#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：DailyCode 
@File    ：01深浅copy.py
@IDE     ：PyCharm 
@Author  ：wangyuqi
@Date    ：2021/6/30 1:08 上午 
'''

# 潜拷贝 :是把原列表第一层的内存地址，不加区分原封不动的拷贝一份给新列表
# list1 = ["abs","ccc",[1,2]]
# list2 = list1.copy()
# print(list2)
# print(id(list1))
# print(id(list2))
# print(id(list1[0]),id(list1[1]),id(list1[2]))
# print(id(list2[0]),id(list2[1]),id(list2[2]))


# 深拷贝

import copy
list1 = ["abs","ccc",[1,2]]
list3 =copy.deepcopy(list1)
print(id(list1))
print(id(list3))
print(id(list1[0]),id(list1[1]),id(list1[2]))
print(id(list3[0]),id(list3[1]),id(list3[2]))