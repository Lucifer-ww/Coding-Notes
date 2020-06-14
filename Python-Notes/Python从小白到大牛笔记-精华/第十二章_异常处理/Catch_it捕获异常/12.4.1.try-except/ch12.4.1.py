# -*- coding: UTF-8 -*-
#!/usr/bin/python3

import datetime as dt

def read_date(in_date):
    try:
        date = dt.datetime.strptime(in_date, '%Y-%m-%d')
        return date
    except ValueError:
        print("ValueError!")

str_date = '2018-8-18'
print("日期 = {0}".format(read_date(str_date)))
