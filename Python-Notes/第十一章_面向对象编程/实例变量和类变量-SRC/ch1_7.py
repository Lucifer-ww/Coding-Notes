#!/usr/bin/env python3
# ch1_7.py
'''
author: Thomaslk
Create Date: 2020-05-25
note: 文章配套代码，认识类方法
'''


class Account:

    interest_rate = 0.0668

    def __init__(self, _owner, _amount):
        self.owner = _owner
        self.amout = _amount

    #类方法
    @classmethod
    def interest_by(cls, amt):
        return cls.interest_rate * amt
    @staticmethod
    def interest_with(amt):
        return Account.interest_by(amt)

#输出自己试