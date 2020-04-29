"""
coder:thomas
coded day:2020.2.27
"""

print("斐波那契数列:")
print("输入到第几次？")

n = int(input("> "))
first_num1 = 1
first_num2 = 1

for item in range(2, n, 1):
    n = first_num2 + first_num1
    first_num1 = first_num2
    first_num2 = n
print(n)


