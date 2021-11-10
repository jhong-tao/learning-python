#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python实例索引操作.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
实例对象索引操作，就是可以像操作列表一样操作实例
必须实现__setitem__  __getitem__  __delattr__ 这三个内置方法
"""


class Person:
    def __init__(self):
        self.cache_dict = {}

    def __setitem__(self, key, value):
        self.cache_dict[key] = value

    def __getitem__(self, item):
        return self.cache_dict[item]

    def __delattr__(self, item):
        del self.cache_dict[item]

    def __str__(self):
        return self.cache_dict.__str__()


one = Person()
one["name"] = "张三"

print(one)

