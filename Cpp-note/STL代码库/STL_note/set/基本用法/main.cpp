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