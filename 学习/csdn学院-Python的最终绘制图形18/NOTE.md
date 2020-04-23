[toc]

## 绘制图形

画五边形、六边形、圆等等
### 调整屏幕大小
```python
import turtle
#todo:调整屏幕大小
turtle.screensize(10, 10)
turtle.showturtle()
turtle.done()
```
### write函数调整字体及字号和用途
实例：
```python
import turtle
turtle.write("hello!", font=("华文琥珀", 80, "normal"))
```
输出一个80号字普通用途的华文琥珀字体的"hello!"

![image-20200407190517499](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200407190517499.png)

### 画圆的步数

circle是画圆函数，然后其中可以调用一个参数step绘制图形

```python
import turtle
turtle.circle(100, step=2000)
```

意思是100的半径，2000步画完！接近一个圆了

如果把steps调成5，就会画成一个五边形

然后这个“海龟”:turtle:就像海龟一样的画啊画:snail:……:snail:

![image-20200407191352958](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200407191352958.png)

画成5边型

![image-20200407191548565](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200407191548565.png)

### 填充颜色

用到函数：

1. begin_fill()     开始填充
2. end_fill()         结束填充
3. reset()                重置      =clear
4. pensize()           笔粗
5. hideturtle()      隐藏箭头

```python
import turtle
turtle.begin_fill()
turtle.circle(100, 5)
turtle.color("blue")
turtle.end_fill()
```

![image-20200407192024560](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200407192024560.png)

```python
...
turtle.pensize(20)
```

![image-20200407192349381](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200407192349381.png)

```python
...
turtle.hideturtle()
```

![image-20200407193806403](C:\Users\33924\AppData\Roaming\Typora\typora-user-images\image-20200407193806403.png)