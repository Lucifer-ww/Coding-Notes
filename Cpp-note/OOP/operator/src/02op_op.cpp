#include <iostream>
using namespace std;
class Date {
public:
    int month;
    int day;
    Date operator-(Date &b)
    {
        Date R;
        R.month = month - b.month;
        R.day = day - b.day;
        return R;
    }
};

Date d1, d2;

int main()
{
    std::cin >> d1.month >> d1.day;
    std::cin >> d2.month >> d2.day;
    Date DateAns = d1 - d2;
    cout << DateAns.month << " " << DateAns.day << endl;
    return 0;
}