#-*- coding = utf-8 -*-

def print_area(width, height):
    area = width * height
    print("{0} x {1} 长方形的面积:{2}".format(width, height, area))

print_area(320.0, 48.0)     # 没有采用关键字参数函数调用
print_area(width = 320.0, height = 480.0)     # 采用关键字参数函数调用
print_area(320.0, height = 480.0)     # 采用关键字参数函数调用
# print_area(width = 32.0, height)     #发生错误
#原因--height没有数值,系统就会认为是一个变量,而这个变量没有定义声明
print_area(height = 480.0, width = 320.0)     #采用关键字参数函数调用
