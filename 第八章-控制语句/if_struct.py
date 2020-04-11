#coding = utf-8
#!/usr/bin/python3

'''if结构'''
print("if\n------------")

import sys

score = int(sys.argv[1])

if score >= 85:
    print("您真优秀")
if score < 60:
    print("您需要加倍努力")
if score >= 60 and score < 85:
    print("您的成绩还可以，仍要继续努力！")

'''if-else结构'''
print("if-else\n------------")


score = int(sys.argv[1])

if score >= 60:
    if score >= 90:
        print("优秀")
    else:
        print("及格")
else:
    print("不及格")


'''elif'''
print("elif\n------------")

score = int(sys.argv[1])

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
	grade = 'F'

print("Grade = " + grade)
