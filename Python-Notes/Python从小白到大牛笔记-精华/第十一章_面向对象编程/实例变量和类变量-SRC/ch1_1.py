# -*- coding: UTF-8 -*-
#!/usr/bin/env python3
'''
author: Thomaslk
Create Date: 2020-05-25
note: 文章配套代码，类的实例变量和类变量，附带继承
'''


class People(object):  # 定义一个People类，名字叫People
    typeof = 'People'  # 类变量，是所有实例共有的变量（这个类变量定义的有点不实际）

    def __init__(self, _sex, _age):  # 构造方法，就先来一个性别和年龄的构造
        self.sex = _sex  # 实例变量
        self.age = _age  # 实例变量
        #必须有self，这是给People这个自己构造，否则就可以只用类变量了



class Student(People):  # 继承了People父类
    def __init__(self, _name, _SN):  # 这时候导入名字和学号
        self.name = _name
        self.Student_Number = _SN

    def PrintYourName(self):
        print("name is:{0}".format(self.name))



class THOMAS(Student):
    pass


cc = People('man', 11)
print("性别：{0}, 年龄：{1}".format(cc.sex, cc.age))
stu = Student('tom', 14)
print("名字：{0}, 学号：{1}".format(stu.name, stu.Student_Number))
stu.PrintYourName()