#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python装饰器.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
装饰器的作用：在原函数不变的情况下，给它增加一些额外的功能
"""
# 定义一个装饰器函数，用来给功能函数添加验证功能
# 将功能函数作为参数传给装饰器函数，在装饰器函数里创建一个闭包内部函数，在闭包里给功能函数添加功能，然后返回闭包函数，这样就完成了给功能函数增加功能的操作
def check_login(f):
    def inner():
        print("登录验证")
        f()
    return inner

# 定义功能函数，发说说和发图片
@check_login        # python语法糖的方式调用装饰器，来给原函数增加新的功能，调用方法：@装饰器函数名
def fss():
    print("发说说")

# # 手动实现，调用装饰器
# fss = check_login(fss)  # 将功能函数传递给装饰器，然后在把装饰后的新函数返回给原函数变量，相当于让原函数变量指向了新的函数

@check_login
def ftp():
    print("发图片")

# 业务逻辑，当btn_index==1的时候发说说，btn_index==2的时候发图片
btn_index = 1
if btn_index == 1:
    fss()
elif btn_index == 2:
    ftp()
