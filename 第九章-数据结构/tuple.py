#-*- coding = utf -8 -*-
#!/usr/bin/python3
#下标访问、索引操作1
a = 'Hello'
print(a[0])
print(a[1])
print(a[2])
for item in range(0, 4):
    print(a[item])
print(max(a))
print(min(a))
print(len(a))
#序列的加和乘、字符串2
a = 'Hello'
print(a * 3)
print(a)
a += ' '
a += 'World'
print(a)
#序列分片、切割3
a = 'Hello'
print(a[1:3])
print(a[:3])
print(a[0:3])
print(a[0:])
print(a[0:5])
print(a[:])
print(a[1:-1])
