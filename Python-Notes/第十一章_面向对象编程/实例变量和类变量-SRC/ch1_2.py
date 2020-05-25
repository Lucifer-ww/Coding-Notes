# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
'''
author: Thomaslk
Create Date: 2020-05-25
note: 文章配套代码，定义实例变量
'''
class Animal(object):
    """定义动物类"""

    def __init__(self, _age, _sex, _weight): #为了区分，将参数加下划线
        self.age = _age
        self.sex = _sex
        self.weight = _weight

conn = Animal(2, 1, 10.0)
# 1是雄性，0是雌性
print('年龄：{0}'.format(conn.age))
print('性别：{0}'.format('雌性' if conn.sex == 0 else '雄性'))
print('体重：{0}'.format(conn.weight))