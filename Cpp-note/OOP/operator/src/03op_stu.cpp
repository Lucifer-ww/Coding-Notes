#include <iostream>
using namespace std;
class stuScore {
private:
    int chinese;
    int math;
    int english;
public:

    void setScore()
    {
        cin >> chinese >> math >> english;
    }
    stuScore operator+(stuScore ss)
    {
        stuScore rb;
        rb.chinese = chinese + ss.chinese;
        rb.math = math + ss.math;
        rb.english = english + ss.english;
        return rb;
    }
    void outScore()
    {
        cout << chinese << " " << math << " " << english << endl;
    }
};
stuScore s1, s2, ans;
int main()
{
    s1.setScore();
    s2.setScore();
    ans = s1 + s2;
    ans.outScore();
    return EXIT_SUCCESS;
}