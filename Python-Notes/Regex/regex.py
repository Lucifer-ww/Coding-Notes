import re

text = ''

file = open("poem.txt")

for line in file:
    text = text + line
file.close()
'''
result = re.findall(" (a[a-z][a-z]) |A[a-z][a-z] ", text)
result = set(result)
'''
result = re.findall("\S", text)
print(result)