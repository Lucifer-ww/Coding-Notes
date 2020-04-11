# -*- coding = utf-8 -*-
#!/usr/bin/python3

print("------范围------")
for num in range(1, 10):
    print("{0} x {0} = {1}".format(num, num * num))
print("------字符串------")
for item in 'Hello':
    print(item)
    
numbers = [43, 32, 53, 54, 75, 7, 10]

print("------整数列表------")
for item in numbers:
    print("Count is : {0}".format(item))