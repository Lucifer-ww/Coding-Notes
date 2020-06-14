# -*- coding: UTF-8 -*-
#!/usr/bin/python3
import os
f = open(r"E:\王一涵programThomas\Coding-Notes\Python-Notes\第十五章-文件操作与管理\OS_Module\3.walk\out\outPutOfWalk.log", 'w+', encoding='UTF-8')
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        f.write(os.path.join(root, name))
    for name in dirs:
        f.write(os.path.join(root, name))
