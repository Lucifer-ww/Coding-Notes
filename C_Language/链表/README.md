# 链表，指针！

结构体可不可以这样

```c
struct Test{
    int x;
    int y;
    struct Test test;
};
```

哦这显然是不行的，这样会陷入无限循环，test的结构体又会指向自己，再次指向，就成了没有出口的递归，但是有一种方法可以解决！

```c
struct Test{
    int x;
    int y;
    struct Test *test;
};
```

这是什么？指针？对就是指针！牛逼吧，一个星号解决问题！