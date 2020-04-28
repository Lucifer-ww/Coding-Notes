# -*- coding = utf-8 -*-

student_list = ['张三', '李四', '王五']
student_list.append('董六')

print(student_list)

student_list += ['刘备', '关羽']

print(student_list)
student_list.extend(['张飞', '赵云'])
print(student_list)

del student_list

student_list = ['张三', '李四', '王五']
student_list[0] = "诸葛亮"
print(student_list)
student_list = ['张三', '李四', '王五', '王五']
student_list.remove('王五')

print(student_list)
student_list.remove('王五')
print(student_list)

student_list.append('王五')
print(student_list)
student_list.pop()
print(student_list)