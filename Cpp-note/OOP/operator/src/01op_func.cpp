#include <iostream>

using namespace std;
void swap(int &a, int &b)
{
    a = a + b;
    b = a - b;
    cout << "swap in func" << endl;
}
int main()
{
    int a = 1, b = 2;
    swap(a, b);
    cout << a << " " << b << endl;
    //输出 2 1    
    return 0;
}