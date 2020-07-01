import random
import time
def pr(a):#用于输出方便阅读的结果
    for i in range(9):
        if i%3==0:
            print('\t---------\t\t---------\t\t---------')
        for j in range(9):
            if j%3==0:
                print('|',end='\t')
            print(a[i][j],end='\t')
        print('|',end='\n')
    print('\t---------\t\t---------\t\t---------')
def diff(d):
    print('数独难度：',end='')
    if d==0:
        print('极容易')
    if d==1:
        print('容易')
    if d==2:
        print('一般')
    if d==3:
        print('困难')
    if d==4:
        print('极困难')
def con(a):#用于将数据转化为符合格式的序列
    if len(a)==81:
        a_con=[[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            b=a[i*9:i*9+9]
            for j in range(9):
                a_con[i].append(int(b[j]))
        return a_con
    return False
def examine_sudoku(sudoku):#检查是否符合数独规则
    if len(sudoku)!=9:
        return False
    for i in range(9):
        if len(sudoku[i])!=9 or sudoku[i].count([])>0:
            return False
        for j in range(1,10):
            if sudoku[i].count(j)>1:
                return False
    return True
def complete(a):#用于检测数独是否完成
    for i in range(9):
        for j in range(9):
            if type(a[i][j])!=int or a[i][j]==0:
                return False
    return True
def copy(a):#复制数独的值，用于后期假设法运算失败，找回原来的值
    d=[[], [], [], [], [], [], [], [], []]
    for i in range(9):
        for j in range(9):
            if type(a[i][j])==int:
                d[i].append(a[i][j])
            elif type(a[i][j])==list:
                d[i].append([])
                for k in a[i][j]:
                    d[i][j].append(k)
    return d
def extract_b_c(a):#用9行表示的a，得到9列表示的b，及9宫表示的c，并对每个0所在的位置用[1,2,3,4,5,6,7,8,9]代替，作为笔记
    b=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    c=[[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                a[i][j] = [1,2,3,4,5,6,7,8,9]
            b[j][i]=a[i][j]
            s=ij_s(i,j)
            c[s].append(a[i][j])
    return b,c
def ij_s(i,j):#用i和j求得宫所在的位置s
    s=i//3*3+j//3
    return s
def ij_t(i,j):#用i和j求得所在宫里的位置t
    t=i%3*3+j%3
    return t
def st_i(s,t):#用s和t求得原i的值
    i=s//3*3+t//3
    return i
def st_j(s, t):#用s和t求得原j的值
    j=s%3*3+t%3
    return j
def play_1(a,b,c,i,j,change):#将笔记中同行、同列及同宫的笔记里删除已知数字，并将唯一可能的格子变成已知数字
    s=ij_s(i,j)
    for num in range(1,10):
        for k in range(9):
            if type(a[i][k])==list and num in a[i] and num in a[i][k]:
                a[i][k].remove(num)
                change=True
                if len(a[i][k])==1:
                    n=a[i][k][0]
                    a[i][k]=n
                    b[k][i]=n
                    c[ij_s(i,k)][ij_t(i,k)]=n
                    change=True
            if type(b[j][k])==list and num in b[j] and num in b[j][k]:
                b[j][k].remove(num)
                change=True
                if len(b[j][k])==1:
                    n=b[j][k][0]
                    a[k][j]=n
                    b[j][k]=n
                    c[ij_s(k,j)][ij_t(k,j)]=n
                    change=True
            if type(c[s][k])==list and num in c[s] and num in c[s][k]:
                c[s][k].remove(num)
                change=True
                if len(c[s][k])==1:
                    n=c[s][k][0]
                    a[st_i(s,k)][st_j(s,k)]=n
                    b[st_j(s,k)][st_i(s,k)]=n
                    c[s][k]=n
                    change=True
    return a,b,c,change
def play_2(a,b,c,i,j,change):#唯一候选数法
    def num_abc():
        num_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num_b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        num_c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for k in range(1,10):
            if k in a[i]:
                num_a.remove(k)
            if k in b[j]:
                num_b.remove(k)
            if k in c[s]:
                num_c.remove(k)
        return num_a,num_b,num_c
    s=ij_s(i,j)
    num_a,num_b,num_c=num_abc()
    for n in num_a:
        t=0
        for k in range(9):
            if type(a[i][k])==list and n in a[i][k]:
                t+=1
        if t==1:
            for k in range(9):
                if type(a[i][k]) == list and n in a[i][k]:
                    a[i][k] = n
                    b[k][i] = n
                    c[ij_s(i, k)][ij_t(i, k)] = n
                    num_a, num_b, num_c = num_abc()
            change=True
    for n in num_b:
        t=0
        for k in range(9):
            if type(b[j][k])==list and n in b[j][k]:
                t+=1
        if t==1:
            for k in range(9):
                if type(b[j][k])==list and n in b[j][k]:
                    a[k][j] = n
                    b[j][k] = n
                    c[ij_s(k, j)][ij_t(k, j)] = n
                    num_a, num_b, num_c = num_abc()
            change=True
    for n in num_c:
        t=0
        for k in range(9):
            if type(c[s][k])==list and n in c[s][k]:
                t+=1
        if t==1:
            for k in range(9):
                if type(c[s][k])==list and n in c[s][k]:
                    a[st_i(s,k)][st_j(s,k)]=n
                    b[st_j(s,k)][st_i(s,k)]=n
                    c[s][k]=n
            change=True
    return a,b,c,change
def play_3(a,b,c,i,j,change):#链数删减法，专业用语是这样的，有2链数、3链数的，此方法扩展到n链数（帮助排除不可能项的）
    list_a=[]
    list_b=[]
    list_c=[]
    s=ij_s(i,j)
    for k in range(9):
        if type(a[i][k]) == list:
            list_a.append(a[i][k])
    for k in range(9):
        if type(b[j][k]) == list:
            list_b.append(b[j][k])
    for k in range(9):
        if type(c[s][k]) == list:
            list_c.append(c[s][k])
    for k in range(3,len(list_a)+1):
        l=[]
        n=0
        for m in list_a:
            if len(m)<k:
                for p in m:
                    if p not in l:
                        l.append(p)
                n+=1
        if len(l)==n:
            for m in list_a:
                for p in m:
                    if p not in l:
                        for q in l:
                            if q in m:
                                m.remove(q)
                                change=True
    for k in range(3,len(list_b)+1):
        l=[]
        n=0
        for m in list_b:
            if len(m)<k:
                for p in m:
                    if p not in l:
                        l.append(p)
                n+=1
        if len(l)==n:
            for m in list_b:
                for p in m:
                    if p not in l:
                        for q in l:
                            if q in m:
                                m.remove(q)
                                change=True
    for k in range(3,len(list_c)+1):
        l=[]
        n=0
        for m in list_c:
            if len(m)<k:
                for p in m:
                    if p not in l:
                        l.append(p)
                n+=1
        if len(l)==n:
            for m in list_c:
                for p in m:
                    if p not in l:
                        for q in l:
                            if q in m:
                                m.remove(q)
                                change=True
    return a,b,c,change
def play_4(a,b,c,change):#区块摒除法
    for i in range(3):
        m = [[], [], [], [], [], [], [], [], []]
        for k in range(3):
            for j in range(9):
                if type(a[i * 3 + k][j]) == list:
                    for n in a[i * 3 + k][j]:
                        if n not in m[k * 3 + j // 3]:
                            m[k * 3 + j // 3].append(n)
        for p in range(3):
            o = []
            for q in range(3):
                if m[p * 3 + q]!=[]:
                    for k in m[p * 3 + q]:
                        if k not in o:
                            o.append(k)
            if o!=[]:
                for s in o:
                    t = 0
                    for q in range(3):
                        if s in m[p * 3 + q]:
                            t += 1
                    if t == 1:
                        for q in range(3):
                            if s in m[p * 3 + q]:
                                if p == 0:
                                    l = [1, 2]
                                elif p == 1:
                                    l = [0, 2]
                                else:
                                    l = [0, 1]
                                for k in l:
                                    for j in range(3):
                                        if type(a[i * 3 + k][q*3+j]) == list and s in a[i * 3 + k][q*3+j]:
                                            a[i * 3 + k][q*3+j].remove(s)
                                            change = True
    for i in range(3):
        m = [[], [], [], [], [], [], [], [], []]
        for k in range(3):
            for j in range(9):
                if type(b[i * 3 + k][j]) == list:
                    for n in b[i * 3 + k][j]:
                        if n not in m[k * 3 + j // 3]:
                            m[k * 3 + j // 3].append(n)
        for p in range(3):
            o = []
            for q in range(3):
                if m[p * 3 + q]!=[]:
                    for k in m[p * 3 + q]:
                        if k not in o:
                            o.append(k)
            if o!=[]:
                for s in o:
                    t = 0
                    for q in range(3):
                        if s in m[p * 3 + q]:
                            t += 1
                    if t == 1:
                        for q in range(3):
                            if s in m[p * 3 + q]:
                                if p == 0:
                                    l = [1, 2]
                                elif p == 1:
                                    l = [0, 2]
                                else:
                                    l = [0, 1]
                                for k in l:
                                    for j in range(3):
                                        if type(b[i * 3 + k][q*3+j]) == list and s in b[i * 3 + k][q*3+j]:
                                            b[i * 3 + k][q*3+j].remove(s)
                                            change = True
    return a,b,c,change
def play_5(a,b,c,change,examine,a_copy):#假设法
    if examine==True:
        for l in range(2,10):
            for i in range(9):
                for j in range(9):
                    if type(a[i][j])==list and len(a[i][j])==l:
                        a_copy=copy(a)
                        n=a[i][j][random.randint(0,len(a[i][j])-1)]
                        a_copy[i][j].remove(n)
                        if len(a_copy[i][j])==1:
                            a_copy[i][j]=a_copy[i][j][0]
                        a[i][j]=n
                        b[j][i]=n
                        c[ij_s(i,j)][ij_t(i,j)]=n
                        change=True
                        return a,b,c,change,examine,a_copy
    if examine==False and examine_sudoku(a_copy)==True:
        a=a_copy
        b,c=extract_b_c(a)
        change=True
        examine=True
        return a,b,c,change,examine,a_copy
    examine=False
    return a,b,c,change,examine,a_copy
def play_all(a,b,c,change,examine,a_copy,d):#进阶型运算，能初级方法解决就不用高级的方法，省时
    for i in range(9):
        for j in range(9):
            a,b,c,change=play_1(a,b,c,i,j,change)
    if change==False:
        for i in range(9):
            for j in range(9):
                a,b,c,change=play_2(a,b,c,i,j,change)
        if d<1 and change==True:
            if complete(a)==False:
                d=1
    if change==False:
        for i in range(9):
            for j in range(9):
                a,b,c,change=play_3(a,b,c,i,j,change)
        if d<2 and change==True:
            if complete(a)==False:
                d=2
    if change==False:
        a,b,c,change=play_4(a,b,c,change)
        if d<3 and change==True:
            if complete(a)==False:
                d=3
    if change==False:
        examine=examine_sudoku(a)
        a,b,c,change,examine,a_copy=play_5(a,b,c,change,examine,a_copy)
        if d<4 and change==True:
            if complete(a)==False:
                d=4
    return a,b,c,change,examine,a_copy,d
def play_all_1(a,b,c,change,examine,a_copy):#进阶型运算，能初级方法解决就不用高级的方法，省时
    for i in range(9):
        for j in range(9):
            a,b,c,change=play_1(a,b,c,i,j,change)
    if change==False:
        for i in range(9):
            for j in range(9):
                a,b,c,change=play_2(a,b,c,i,j,change)
    if change==False:
        for i in range(9):
            for j in range(9):
                a,b,c,change=play_3(a,b,c,i,j,change)
    if change==False:
        a,b,c,change=play_4(a,b,c,change)
    return a,b,c,change,examine,a_copy
def complate_sudoku(a):#计算数独的主体
    if examine_sudoku(a)==False:
        return False
    b,c = extract_b_c(a)
    if examine_sudoku(b)==False:
        return False
    if examine_sudoku(c)==False:
        return False
    change = True#初始化change
    examine=True#初始化examine
    a_copy=[]#初始化a_copy
    d=0
    while change==True:
        change=False
        a,b,c,change,examine,a_copy,d=play_all(a,b,c,change,examine,a_copy,d)
        examine=examine_sudoku(a)&examine_sudoku(b)&examine_sudoku(c)
    if complete(a)==False:
        return None,4
    return a,d
print('正在生成数独......')
t=time.time()
a=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for j in range(9):
    if j<8:
        k=random.randint(0,len(l)-1)
        a[0][j]=l[k]
        del l[k]
    else:
        a[0][j] = l[0]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.remove(a[0][0])
l.remove(a[0][1])
l.remove(a[0][2])
for i in range(1,9):
    if i==3:
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        l.remove(a[0][0])
        l.remove(a[1][0])
        l.remove(a[2][0])
    if i<8:
        k=random.randint(0,len(l)-1)
        a[i][0]=l[k]
        del l[k]
    else:
        a[i][0] = l[0]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.remove(a[0][6])
l.remove(a[0][7])
l.remove(a[0][8])
for i in range(1,9):
    if i==3:
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        l.remove(a[0][8])
        l.remove(a[1][8])
        l.remove(a[2][8])
    if i<8:
        if i==7:
            if a[8][0] in l:
                a[7][8]=a[8][0]
                l.remove(a[8][0])
                a[8][8]=l[0]
                break
        k=random.randint(0,len(l)-1)
        while l[k]==a[i][0]:
            k = random.randint(0, len(l) - 1)
        a[i][8]=l[k]
        del l[k]
    else:
        a[i][8] = l[0]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l.remove(a[8][0])
l.remove(a[8][8])
b, c = extract_b_c(a)
a_copy2=[]
d=0
change = True  # 初始化change
examine = True  # 初始化examine
a_co = []  # 初始化a_copy
while change == True:
    change = False
    a, b, c, change, examine, a_co ,d= play_all(a, b, c, change, examine, a_co,d)
print('数独答案生成完毕，开始抠除数字......')
ti=0
com=copy(a)
change = True  # 初始化change
x=True
co=copy(a)
l=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
   27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
   54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
while x==True:
    change = True  # 初始化change
    examine = True  # 初始化examine
    a_co = []  # 初始化a_copy
    if len(l)>1:
        k=random.randint(0,len(l)-1)
    else:
        k=0
        x=False
    p=l[k]//9
    q=l[k]%9
    del l[k]
    if co[p][q]==0:
        continue
    co[p][q]=0
    cop=copy(co)
    cop_b, cop_c = extract_b_c(cop)
    while change == True:
        change = False
        cop, cop_b, cop_c, change, examine, a_co= play_all_1(cop, cop_b, cop_c, change, examine, a_co)
    if complete(cop)==True:
        a = copy(co)
    else:
        if ti==0:
            print('一般难度已生成，正在精细推敲骨灰难度......')
            ti=1
        for i in range(9):
            for j in range(9):
                if type(cop[i][j])==list and len(cop[i][j])==2:
                    a_copy=copy(cop)
                    n=cop[i][j][0]
                    a_copy[i][j]=a_copy[i][j][1]
                    a_copy_b, a_copy_c = extract_b_c(a_copy)
                    cop[i][j]=n
                    cop_b[j][i]=n
                    cop_c[ij_s(i,j)][ij_t(i,j)]=n
                    change=True
                    while change == True:
                        change = False
                        cop, cop_b, cop_c, change, examine, a_co,d=play_all(cop, cop_b, cop_c, change, examine, a_co,d)
                    while change == True:
                        change = False
                        a_copy, a_copy_b, a_copy_c, change, examine, a_copy2,d=play_all(a_copy, a_copy_b, a_copy_c, change, examine, a_copy2,d)
                    if (complete(cop)==True and complete(a_copy)==False) or (complete(cop)==False and complete(a_copy)==True):
                        if cop==com or cop==com:
                            a = copy(co)
print('数独生成完毕，生成数独所用时间为：',time.time()-t)
pr(a)
t=time.time()
a,d=complate_sudoku(a)
print('解数独所用时间为：',time.time()-t)
diff(d)
pr(a)