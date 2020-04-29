### C++中Sort函数

c++中的Sort函数默认排序为程序，那么怎么改成降序呢？

#### 自己编写*Compare*函数

```cpp
#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
bool compare(int a, int b) {
    return a < b;
}
int main()
{
    int n;
    cin >> n;
    int a[1001];
    for (int i = 0; i < n; i ++) {
        cin >> a[i];
    }
    cout << "input is:" << endl;
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    sort (a, a + n, compare);
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;
    return 0;
}
```

