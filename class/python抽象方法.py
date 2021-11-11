#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> python抽象方法.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
import abc

"""
需要导入abc模块
抽象类的元类需要继承abc.ABCMeta模块
"""


class Animal(object, metaclass=abc.ABCMeta):
    # 必须要实现的抽象接口
    @abc.abstractmethod
    def eat(self):
        pass


class Dog(Animal):
    # 子类必须实现父类的抽象方法
    def eat(self):
        print("吃饭")


dog = Dog()
dog.eat()
