# -*-coding: UTF-8 -*-
#!/usr/bin/python3

f = open('test.txt', 'w+')
f.write('World')

f = open('test.txt', 'r+')
f.write('Hello')

f = open('test.txt', 'a')
f.write(' ')

fname = r'E:\王一涵programThomas\王一涵PythonThomas\Python-Learned\第十五章-文件操作与管理\文件操作代码01\test.txt'
f = open(fname, 'a+')
f.write('World');