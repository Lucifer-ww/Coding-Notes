<center><h3>Vector动态数组字符类型-整行输入</h3></center>

[TOC]

### 问题描述

​	我们在字符串输入的时候，如果要输入一行字符，就直接用`std::cin`就可以，但是如果要输入*hello world*呢？就要用到[getline()](https://blog.csdn.net/cool99781/article/details/104595125)整行输入，getline或cin.getline的详细介绍见前面的链接。

​	但是，我们用vector的char类型动态数组怎么整行输入呢？我们知道，C语言中没有string类型，字符数组就是字符串，可以用`cin.getline(ch, 500)`这种方式整行输入，但vector不支持getline，下面详细介绍。

### 解决方法

#### 1.自己写函数

​	没有函数库，就自己写函数库嘛，对不:smile:

​	如果我们用c++开发，先定义一个string字符串，然后先用string的getline(std::cin, str);然后再建立一个函数$$vectorSetValue()$$读入字符数组，然后遍历字符串，把每一个字符push_back()进字符数组，就成了,见下面代码

#### 2.

### 代码

#### Solution

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void vectorSetValue(vector<char>&aVec, string aStr){
    for (int i=0; i< aStr.size(); i++){
        aVec.push_back(aStr[i]);
    }
}

void showVector(vector<char>&aVec){
    for (int i=0; i< aVec.size(); i++){
        cout << aVec[i];
    }    
}
int main(){
    vector <char> s1;
    string s2;
    getline(cin, s2);
    vectorSetValue(s1, s2);
    showVector(s1);
    return 0;    
}
```

