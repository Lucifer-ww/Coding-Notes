#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    vector<int> sortv; //动态数组
    for (int i = 0; i < 5; i++)
    {
        int t;
        cin >> t;
        sortv.push_back(t);
    }
    sort(sortv.begin(), sortv.end());
    for (int i = 0; i < 5; i++)
    {
        cout << sortv[i] << endl;
    }
    //数组
    int sortnums[6];
    for (int i = 0; i < 5; i++)
        cin >> sortnums[i];
    sort(sortnums, sortnums + 5);
    for (int i = 0; i < 5; i++)
        cout << sortnums[i] << endl;
    //此sort是升序排序
    return 0;
}