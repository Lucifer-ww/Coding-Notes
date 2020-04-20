# coding=utf-8
#!/usr/bin/python3

import random

# 0.0 <= x < 1.0随机数
print('0.0 <= x < 1.0随机数')
for i in range(0, 10):
    x = random.random()
    print(x)
    pass

# 0 <= x < 5随机数
print('0 <= x < 5随机数')
for i in range(0, 10):
    x = random.randrange(5)
    print(x, end=' ')
    pass
print()

# 5 <= x < 10随机数
print('5 <= x < 10随机数')
for i in range(0, 10):
    x = random.randrange(5, 10)
    print(x, end=' ')
    pass
print()
