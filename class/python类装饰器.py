#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python类装饰器.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
装饰器的实现方式有两种
方式一：基于函数的闭包形式
方式二：基于类的形式，实现__init__和__call__方法
"""


# 方式一：闭包形式，把原函数，传递个装饰器函数
def check(func):
    def inner(*args, **kwargs):
        print("装饰器一：登录验证")  # 给原函数增加新的操作
        return func(*args, **kwargs)  # 执行原函数

    return inner  # 返回新的函数


# 方式二：类装饰器，实现类的__init__函数和__call__函数
class Check:
    # 需要将原函数传递个 类的构造方法，将原函数保存成为类的一个方法
    def __init__(self, func):
        self.func = func

    # 为了使装饰器类能被调用，需要实现__call__方法，同时在__call__方法中给原函数添加新的功能，并调用原函数
    def __call__(self, *args, **kwargs):
        print("装饰器二：登录验证")  # 增加新的功能
        return self.func(*args, **kwargs) # 执行原函数

@check
def base(a, b):
    print(a + b)


base(1, 2)

@Check
def base1(a, b):
    print(a + b)


base1(1, 2)