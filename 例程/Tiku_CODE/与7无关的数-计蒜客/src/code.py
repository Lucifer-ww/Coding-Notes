# -*- coding = UTF -8 -*-
n = int(input()) #输入范围
ans = 0
for item in range(n):
    tmps = str(item)
    flag = False #默认跟7无关
    for index in tmps:
        temp = int(index)
        if temp == 7:
            flag = True #设置为有关
    if int(tmps) % 7 == 0 or flag == True:
        pass
    else:
        ans += item ** 2

print(ans)