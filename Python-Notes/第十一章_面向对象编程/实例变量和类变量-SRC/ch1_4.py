#!/usr/bin/env python3
# ch1_4.py
'''
author: Thomaslk
Create Date: 2020-05-25
note: 文章配套代码，认识构造方法
'''

class Animal(object):
    def __init__(self, age, sex = 1, weight = 0.0):
        self.age = age
        self.sex = sex
        self.weight = weight
a1 = Animal(2, 0, 10.0)
a2 = Animal(1, weight=5.0)
a3 = Animal(1, sex=0)