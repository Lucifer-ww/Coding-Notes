# -*- coding = utf-8 -*-

def square(num):

    for i in range(1, num + 1):
        yield i * i

def out(num):
    for i in range(1, num):
        yield i

item = int(input("$ "))
for i in square(item):
    print(i, end = ' ')

print("\n")
print("1 - 5")

n_seq = out(10)
for i in n_seq:
    print(i, end = ' ')  # n_seq.__next__()
