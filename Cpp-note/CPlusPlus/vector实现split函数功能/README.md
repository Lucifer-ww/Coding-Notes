# 使用C++实现Python的split功能，以字符划分字符串

用vector就行，每次使用getline的特性，判断到空格就终止输入，如下
```cpp
#include <vector>
using namespace std;
vector<string> split(string aStr, char aDem = ' ') {
     vector<string> sv;
     sv.clear();
     stringstream res(aStr);
     string temp;
     while (getline(res, temp, aDem)) {
         sv.push_back(temp);
     }
     return sv;
}
```
这不是就行了，如果你想做到Python那样的**.split()，那么你只需要放在类里面就行