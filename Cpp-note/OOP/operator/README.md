# C++函数以及运算符重载
C++中运算符重载是一个很重要的部分，我们已经知道了函数怎样重载

所谓重载，就是将一个已经定义好的函数、符号等重新定义。

C++在C的基础上增加了重载运算符的能力，而Java不允许修改运算符的含义，但是应该让修改函数。

## 函数重载
首先来看看函数怎样重载：

```cpp
#include <iostream>

using namespace std;
void swap(int &a, int &b)
{
    a = a + b;
    b = a - b;
    cout << "swap in func" << endl; //测试
}
int main()
{
    int a = 1, b = 2;
    swap(a, b);
    cout << a << " " << b << endl;
    //输出 2 1
    return 0;
}
```
如果你觉得没有走自定义的函数，就加上`cout << "swap in func" << endl;`这一句，输出就是这样：
```
swap in func
3 1
```
说明确实走的自定义函数中的交换。这就是重新定义了函数

## 重载运算符

如果有两个日期类，分别存储月日，我们怎么样把这两个类相减放到另一个类里，得出一个日期差？

首先这个类的定义如下
```cpp
class Date {
public:
    int month;
    int day;
};
Date d1, d2;
```
那么总不能直接`d1 - d2`吧，这样异常满天飞，所以需要重新定义减号，其实结构体应该也可以重载。

```cpp
class Date {
public:
    int month;
    int day;
    Date operator-(Date &b)
    {
        Date R;
        R.month = month - b.month;
        R.day = day - b.day;
        return R;
    }
};
```
当然这个operator相当简陋，要是就这样做日期差，会得出负数，而且月份也没有确定啊，所以就得改进，还不如叫减法程序呢

还来个小实例，把两个学生的成绩相加，其实着用个结构体，一个一个加就可以了，不过我为了练练类，和共用和私有，就用这样了
```cpp
#include <iostream>
#include <stdlib.h>
using namespace std;
class stuScore {
private:
    int chinese;
    int math;
    int english;
public:

    void setScore()
    {
        cin >> chinese >> math >> english;
    }
    stuScore operator+(stuScore ss)
    {
        stuScore rb;
        rb.chinese = chinese + ss.chinese;
        rb.math = math + ss.math;
        rb.english = english + ss.english;
        return rb;
    }
    void outScore()
    {
        cout << chinese << " " << math << " " << english << endl;
    }
};
stuScore s1, s2, ans;
int main()
{
    s1.setScore();
    s2.setScore();
    ans = s1 + s2;
    ans.outScore();
    return EXIT_SUCCESS;
}
```