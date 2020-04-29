# -*- coding: UTF-8 -*-
#!/usr/bin/python3

f_name = 'test.txt'

with open(f_name, 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    print(lines)
    print('lines的类型是:', type(lines))
    copy_f_name = 'copy.txt'
    with open(copy_f_name, 'w', encoding='utf-8') as copy_f:
        copy_f.writelines(lines)
        print('文件复制成功')