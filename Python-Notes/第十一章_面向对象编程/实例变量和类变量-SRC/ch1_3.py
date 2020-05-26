# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
# ch1_3.py
'''
author: Thomaslk
Create Date: 2020-05-25
note: 文章配套代码，认识类变量
'''

class Account:
    """定义银行账户类"""

    interest_rate = 0.0668 #类变量——利率

    def __init__(self, _owner, _amount):
        self.owner = _owner
        self.amount = _amount

act = Account('Tony', 1_800_000.0)

#自己输出验证吧