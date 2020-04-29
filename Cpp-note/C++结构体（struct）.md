## C++结构体（struct）

:cloud:<font color=tomato>经典实例：</font>
&emsp;如果要存储一个学生的成绩情况，比如记录语数英的三科成绩，用数组是不行的，因为数组只能存储一种元素的序列而且是同一类型的序列，除非你建立三个数组，但这样也不行，因为数组不是动态的，但是可以试试`vector<vector<int>>`，struct可以实现，因为结构可以将很多数据（可以不同类型）集合在一个单元中。

下面的结构体可以轻松实现学生统计

```cpp
struct student{
	float chinese;
    float math;
    float english;
};
```

这个结构体定义了三个元素：语文成绩、数学成绩和英语成绩
student是新定义的类型名，<font color=red>注意最后要加上分号</font>

:cloud:<font color=tomato>怎么定义一个结构体变量？</font>

封装好一个结构体，调用的时候如下方法

```cpp
student n; //c++
struct student n; //c
```

C++省略了声明时的struct

**初始化**

```cpp
student n={97.5, 98.0, 80.5};
```



:cloud:<font color=tomato>调用方法？</font>

声明之后就可以使用了，怎么使用？
实例：（还是刚才的student结构）

```cpp
cin >> n.chinese; //例如97.5
cin >> n.math;
cin >> n.english;
cout << n.chinese << " " << n.math << " " << n.english << endl;
```

就这样