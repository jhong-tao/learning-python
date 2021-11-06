#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python带参数的装饰器.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
带参数的装饰器，就是要去定义一个装饰器生成函数，根据不同的参数生成不同的装饰器函数
"""
# 定义一个可以传递参数的装饰器生成函数，根据传递不同的参数来实现不同的装饰功能
def get_zsq(char):
    def zsq(base):      # 创建一个装饰器函数
        def inner(*args, **kwargs):     # 创建一个闭包装饰器
            print(char * 30)            # 根据不同的参数来实现不同的装饰功能
            return base(*args, **kwargs)    # 将装饰后计算的结果返回
        return inner        # 返回装饰后的函数
    return zsq      # 返回装饰器函数

@get_zsq("*")       # @get_zsq("*") ，get_zsq("*")就是用来产生装饰器函数zsq的，@get_zsq("*")就等同于base=zsq(base)
def base(a, b):
    print(a + b)
    return a+b

@get_zsq("+")
def base2(a):
    print(a*2)
    return a*2

res = base(1, 2)

res1 = base2(2)
