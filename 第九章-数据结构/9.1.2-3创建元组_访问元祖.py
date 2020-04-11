#coding = utf-8

a = (20)
print(type(a))

a = (20,)
print(type(a))
#tuple

a = (20, 30, 40, 50, 60)
print(a)
print(a[1])
print(a[1:3])

a = ('Hello', 'World', 1, 2, 3)
str1, str2, n1, n2, n3 = a
print(str1)
print(str2)
print(n1, "", n2, "", n3)

str1, str2, *n = a
print(n)