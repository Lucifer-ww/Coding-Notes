#-*- coding = utf-8 -*-

def show_info(sep = ':', **info):    #可变参数,下面讲一下
    """定义**可变参数函数, dict"""
    print('-----info-----')
    for key, value in info.items():
        print('{0} {2} {1}'.format(key, value, sep))
        return                  #return None

result = show_info('->', name = 'Tony', age = 18, sex = True)
print(result)


def sum(*numbers, multiple = 1):
    """定义*可变参数函数, tuple"""
    if len(numbers) == 0:
        return
    total = 0.0
    for number in numbers:
        total += number
    return total * multiple

print(sum(30.0, 80.0))
print(sum(multiple = 2))
