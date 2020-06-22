#tip13: 全局变量 vs 局部变量 global vs local
a = 8

def f1():
	print(a)

def f2():
	print(a)
	a = 18

def f3():
	a = 18
	print(a)

def f4():
	global a
	a = 18
	#print(a)
#f1()
#f2()
#f3()
# f4()
# print(a)

# ### 知识总结 ###
# 全局变量是在函数外定义的变量
# 函数内可以直接访问全局变量
# 函数内定义的变量是局部变量
# 同名的局部变量会覆盖全局变量
# 函数内修改全局变量需要用global
# 全局变量不是真的全局，只是在模块内全局
