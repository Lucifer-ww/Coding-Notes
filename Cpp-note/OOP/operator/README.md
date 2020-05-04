# C++函数以及运算符重载
C++中运算符重载是一个很重要的部分，我们已经知道了函数怎样重载

所谓重载，就是将一个已经定义好的函数、符号等重新定义。

C++在C的基础上增加了重载运算符的能力，而Java不允许修改运算符的含义，但是应该让修改函数。

首先来看看函数怎样重载：

```cpp
#include <iostream>

using namespace std;
void swap(int &a, int &b)
{
    a = a + b;
    b = a - b;
}
int main()
{
    int a = 1, b = 2;
    swap(a, b);
    cout << a << " " << b << endl;
    return 0;
}
```
>STDOUT:<br>输出 2 1 