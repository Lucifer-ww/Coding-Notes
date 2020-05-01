def check(num):
    count = 0;
    for i in range(1, num): 
        print("i:{0}".format(i)) #测试，删掉
        if num % i == 0:
            count += 1
    if count == 1: #由于Python是从1到num减一所以改变了旧方法，如果是质数，只有一个
        return True
    else:
        return False # 合数
nums = []
ans = []
s = input()
nums = s.split(',')
for idx in nums:
    mark = check(int(idx))
    print("idx:{0}, mark:{1}".format(idx, mark)) #测试，删掉
    if not mark:
        ans.append(int(idx))
print(len(ans))