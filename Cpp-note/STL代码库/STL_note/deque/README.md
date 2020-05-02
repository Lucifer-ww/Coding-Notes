# C++STL标准库——双端队列deque
其实deque的最大特点就是<font color=orangered>双端</font>，其可以实现队首队尾都插入的功能

## 对比各种stl容器的存取难度
1. vector：只能插入在队首，但是提供下标访问方式。:star::star::star:
2. stack：不支持下标访问，存入只能存进栈顶，取出最后一个必须一个一个pop。:star:
3. queue：只能插入进队首，不支持下标:star::star:
4. array：类似数组（几乎就是），支持下标，可在任何地方插入:star::star::star::star::star:
5. deque：支持任意地方插入（insert），不支持下标，可在队首队尾插入:star::star::star::star:

从列表中可见deque的存取效率非常高，<small>注：个人认为</small>
## 用法
| 方法          | 含义                                                         |
| ------------- | ------------------------------------------------------------ |
| deque         | 构造函数                                                     |
| push_back     | 在当前的最后一个元素之后 ，在 deque 容器的末尾添加一个新元素 |
| push_front    | 在 deque 容器的开始位置插入一个新的元素，位于当前的第一个元素之前 |
| pop_back      | 删除 deque 容器中的最后一个元素，有效地将容器大小减少一个    |
| pop_front     | 删除 deque 容器中的第一个元素，有效地减小其大小              |
| emplace_front | 在 deque 的开头插入一个新的元素，就在其当前的第一个元素之前  |
| emplace_back  | 在 deque 的末尾插入一个新的元素，紧跟在当前的最后一个元素之后 |
实例：
```cpp
#include <iostream>
#include <deque>
int main ()
{
  unsigned int i;
  // constructors used in the same order as described above:
  std::deque<int> first;                                // empty deque of ints
  std::deque<int> second (4,100);                       // four ints with value 100
  std::deque<int> third (second.begin(),second.end());  // iterating through second
  std::deque<int> fourth (third);                       // a copy of third
  // the iterator constructor can be used to copy arrays:
  int myints[] = {16,2,77,29};
  std::deque<int> fifth (myints, myints + sizeof(myints) / sizeof(int) );
  std::cout << "The contents of fifth are:";
  for (std::deque<int>::iterator it = fifth.begin(); it!=fifth.end(); ++it)
    std::cout << ' ' << *it;
  std::cout << '\n';
  return 0;
}
```
OUT:
```
The contents of fifth are: 16 2 77 29 
```
实例2：
```cpp
#include <iostream>
#include <deque>
int main ()
{
  std::deque<int> mydeque;
  int myint;
  std::cout << "Please enter some integers (enter 0 to end):\n";
  do {
    std::cin >> myint;
    mydeque.push_back (myint);
  } while (myint);
  std::cout << "mydeque stores " << (int) mydeque.size() << " numbers.\n";
  return 0;
}
```
OUT:
```
Please enter some integers (enter 0 to end):1 2 3 4 5 0
mydeque stores 6 numbers.
```