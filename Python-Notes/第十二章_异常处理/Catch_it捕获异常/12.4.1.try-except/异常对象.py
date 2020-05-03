# -*- coding: UTF-8 -*-
#!/usr/bin/python3

import datetime as dt


def read_date(in_date):
    try:
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError as e:
        print("ValueError!")
        print("异常对象：", e)


str_date = '201B-8-18'
print("日期 = {0}".format(read_date(str_date)))