#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main()
{
    vector<int>array;//动态数组
    for (int i = 0; i < 5; i++)
    {
        int t;
        cin >> t;
        array.push_back(t);
    }
    reverse(array.begin(), array.end());
    for (int i = 0; i < array.size(); i++)
        cout << array[i] << " ";
    cout << endl;
    cout << "--------" << endl;
    string str = "hello world";//字符串
    reverse(str.begin(), str.end());
    cout << str << endl;
    cout << "--------" << endl;
    int arr1[101]; //数组
    for (int i = 0; i < 5; i++)
    {
        cin >> arr1[i];
    }
    reverse(arr1, arr1 + 5);
    for (int i = 0; i < 5; i++)
    {
        cout << arr1[i] << " ";
    }
    cout << endl;
    return 0;
}