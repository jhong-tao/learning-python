#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
==================================================
@Project -> File   ：learning-python -> 01-综合案例.py
@IDE    ：PyCharm
@Author ：jhong.tao
@Date   ：2021/6/7 10:34
@Desc   ：
==================================================
"""
from win32com import client


# 计算器，实现加减运算
class Caculator():
    def __speaker(self, word):
        """
        声音播报器
        :param word:
        :return:
        """
        speaker = client.Dispatch("SAPI.SpVoice")
        speaker.speak(word)

    def __say(*args):
        """
        根据不同的计算法方法播报不同的语言的装饰器生成器
        :param args:
        :return:
        """
        def speaker(func):
            """
            语音装饰器
            :param func:
            :return:
            """
            def inner(self, *iargs):
                self.__speaker(str(*args) + str(*iargs))
                return func(self, *iargs)

            return inner

        return speaker

    def __check(func):
        """
        输入数字检查装饰器
        :return:
        """
        def inner(self, num):
            if not isinstance(num, int):
                raise TypeError("数据类型错误")
            return func(self, num)

        return inner

    @__check
    @__say()
    def __init__(self, num):
        self.__res = num

    @__check
    @__say("加")
    def jia(self, num):
        self.__res += num
        return self         # 链式调用方式

    @__check
    @__say("减")
    def jian(self, num):
        self.__res -= num
        return self

    def show(self):
        self.__speaker(str("等于%d" % self.__res))
        print(self.__res)
        return self

    def clear(self):
        self.__speaker(str("清除"))
        self.__res = 0

    @property   # get 方法
    def result(self):
        return self.__res


c1 = Caculator(1).jia(3)
c1.show()
c1.clear()
