#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python对象属性相关.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
"""
类的定义，通过类实例化对象，给对象动态的增加新属性
"""


# 1. 定义一个类
class Person:
    pass


# 2. 根据类实例化一个对象
p = Person()

# 3. 直接通过对象名.属性名的方式给对象添加新的属性
p.age = 18		# 通过对象名.属性名的方式给当前对象p新增一个属性age并给其赋值
p.name = "zs"
p.age = 20      # 通过对象名.属性名的方式访问对象的属性，并修改对象的属性
p.pets = [1, 2, 3]   # 给对象增加一个属性，值的类型是列表
p.pets.append(4)     # 访问对象的可变类型的属性，调用该属性类型自己的方法来修改对象属性的值，此时对象的属性名不会改变指向
p.pets = [1,2]       # 通过访问对象的属性，并给该属性赋予新的值，此时该属性名的指向发生了改变，指向了新的值的内存地址
del p.age            # 通过del语句删除对象的属性

# 4. 直接通过对象名.属性名的方式调用对象的属性
print(p.name)
