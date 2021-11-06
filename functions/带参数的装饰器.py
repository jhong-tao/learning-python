#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> 带参数的装饰器.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
带参数的装饰器，固定的写法
"""
def zsq(f):
    def inner(*args, **kwargs):         # 因为原函数需要参数，而我们的装饰器可以装饰多个函数，不知道原函数到底有几个参数，所以写成可变参数
        print("*"*20)
        f(*args, **kwargs)          # 这里是执行原函数，那么原函数是什么样的，这里就是什么样的，由于inner()里对参数进行了装包，这里原封不动的进行拆包就可以
    return inner

@zsq        # base = zsq(base)
def base(a, b):
    print(a+b)

@zsq
def base2(a, b, c):
    print(a+b+c)

base(1, 2)

base2(1, 2, 3)