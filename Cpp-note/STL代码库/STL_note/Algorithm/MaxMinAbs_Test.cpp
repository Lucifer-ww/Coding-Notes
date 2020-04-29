#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;
    cout << max(a, b) << endl;
    cout << min(a, b) << endl;
    cout << abs(a - b) << endl;
    cout << "-----" << endl;
    return 0;
}