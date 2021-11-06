#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> 装饰器的叠加.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
装饰器的叠加，也就是给函数一层一层的加功能，就像穿衣服一样
从下到上给函数添加装饰器
"""
# 装饰器1，在执行基本函数之前打印-
def line(f):
    def inner():
        print("-"*20)
        f()
    return inner

# 装饰器2 在执行基本函数之前打印+
def line2(f):
    def inner():
        print("+"*20)
        f()
    return inner

@line2      # 添加第二层装饰，就是在第一层装饰的基础上在先打印"+",结果就是先打印“+”，在打印“-”，在打印基本功能
@line       # 添加第一层装饰 就是打印了“-”在打印基本功能
def base():
    print("基本功能")


base()