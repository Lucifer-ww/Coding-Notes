# C++集合-初识Set

<font color=red>Set</font>是C++中模板库的一个STL库，Set就像英文中的意思一样是<font color=red>集合</font>[^1]，关于集合必须说明set是<font color=red>关联式容器</font>。set作为<font color=red>容器</font>，也是用来存储同一数据类型的数据类型，并且能从一个数据集合中取出数据，在set中每个元素的值<font color=red>都唯一</font>，而且系统能够根据元素的值自动进行排序。应该注意的是set中的值<font color=red>不能被直接改变</font>。
C++ STL中标准关联容器set, multiset, map, multimap内部采用的就是一种非常高效的平衡检索二叉树：<font color=red>红黑树，也成为RB树(Red-Black Tree)</font>。RB树的统计性能要好于一般平衡二叉树，所以被STL选择作为了关联容器的内部结构。

## 为什么map和set的插入删除效率比用其他序列容器高？

因为对于关联容器来说，不需要做内存拷贝和内存移动。set容器内所有元素都是以节点的方式来存储，其节点结构和链表差不多，指向父节点和子节点。结构图可能如下：

```
　  A
　 / \
  B   C
 / \ / \
D  E F  G
```
## set常用方法

<pre><strong>
begin()——返回set容器的第一个元素
end()——返回set容器的最后一个 元素
clear()——删除set容器中的所有的元素
empty()——判断set是否为空，返回类型为布尔
max_size()——返回set可能包含的元素最大个数
size()——返回当前set容器中的元素个数
rbegin()——返回的值和end()相同
rend()——返回的值和rbegin()相同
</strong></pre>
**引入头文件：**

需要调用STL库：`#include <set>`

来写一个程序练一练其基本用法

```cpp
#include <iostream>
#include <set>

using namespace std;

int main()
{
    set<int> myset;
    for (int i = 0; i < 10; i++)
        myset.insert(10 - i);
    
    cout << "第一个元素:" << endl;
    cout << *myset.begin() << endl; //星号
    cout << "最后一个元素:" << endl;
    cout << *myset.end() << endl;
    cout << "是否为空?" << endl;
    cout << boolalpha << myset.empty() << endl;
    cout << "元素个数：" << endl;
    cout << myset.size() << endl;
    cout << "某个值元素的个数：" << endl;
    cout << myset.count(1) << endl;

    //删除
    myset.erase(myset.begin());
    myset.erase(2);

    //遍历set集合
    set<int>::iterator it1; //迭代器
    for (it1 = myset.begin(); it1 != myset.end(); it1++)
        cout << *it1 << endl;
    return 0;
}
```

运行结果：

```
第一个元素:
1
最后一个元素:
10
是否为空?
false
元素个数：
10
某个值元素的个数：
1
3
4
5
6
7
8
9
10
```

代码中的*是指针，代表<span style="background-color: Orange">迭代器（iterator）</span>，有一些不用迭代器，所以不需要星号。


[^1]:n. （物品的）一套，一组，一副；一伙（或一帮）人，团伙，阶层；电视机，收音机；布置，场景，舞台；（网球、排球比赛等的）盘，局；（数学中的）集，集合；一组歌曲（乐曲）；（能力相当的）一批学生；（尤指坚定的）姿势，神情；做头发；凝固，凝结；兽穴；（供移植的）秧苗，插枝；装置