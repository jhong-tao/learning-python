#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python函数高级.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
# 偏函数
"""
当一个函数有多个参数时，如果在不同的场景中，函数的某个或者某几个参数是固定的
那么久可以在定义一个函数，让新定义的函数去调用基本函数，在新函数的参数列表中，
把固定值的参数，给它传递默认值
"""

def f_base(a:int, b:int, c:int)->int:
    """
    计算a, b, c 的和
    :param a: 数值1，int类型，不可选，没有默认值
    :param b: 数值2，int类型，不可选，没有默认值
    :param c: 数值3，int类型，不可选，没有默认值
    :return: 返回a,b,c的和，int类型
    """
    return (a + b +c)

# 手工偏函数
def f_phs(a:int, b:int=1,c:int=2)->int:
    """
    f_base的偏函数，设定了b默认为1，c默认为2
    """
    return f_base(a, b, c)

# print(f_phs(1))

# 直接使用python的functools库的partial创建偏函数
from functools import partial
new_f_base = partial(f_base, c=1)
res = new_f_base(2,3)
print(res)
