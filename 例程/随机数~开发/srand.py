# -*- coding = UTF-8 -*-

import random
print(random.randint(1, 10))

print("下面正式进入猜数环节\n计算机想好了一个1-100的数字\n可劲的猜，猜，猜!")
Computer_Num = random.randint(1, 100)
Count = 0
n = 0

while n != Computer_Num:
    n = int(input("input> "))
    if n > Computer_Num:
        print("大了!")
        Count = Count + 1
    elif n < Computer_Num:
        print("小了!")
        Count = Count + 1
    else:
        print("答对了")
        print("猜了{0}次".format(Count + 1))
        break
