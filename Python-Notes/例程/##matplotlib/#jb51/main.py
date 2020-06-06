# -*- coding:utf-8 -*-
#! python3
import numpy as np
import matplotlib.pyplot as plt
# ==========================================
# 圆的基本信息
# 1.圆半径
r = 2.0
# 2.圆心坐标
a, b = (0., 0.)
# ==========================================
# 方法一：参数方程
theta = np.arange(0, 2*np.pi, 0.01)
x = a + r * np.cos(theta)
y = b + r * np.sin(theta)
fig = plt.figure() 
axes = fig.add_subplot(111) 
axes.plot(x, y)
axes.axis('equal')
plt.title('www.jb51.net')

plt.show()
