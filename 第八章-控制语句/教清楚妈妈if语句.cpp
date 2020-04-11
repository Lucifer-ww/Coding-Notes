#include <iostream>

using namespace std;

int main()
{
    int SrandNumber;
    cin >> SrandNumber;//80
    if(SrandNumber > 10)
        cout << "above 10" << endl;
    if(SrandNumber > 20)
        if(SrandNumber > 30)
            if(SrandNumber > 40){
                cout << "above 40" << endl;
                cout << "above 30" << endl;
                cout << "above 20" << endl;
            }
            else{
                cout << "above 30" << endl;
                cout << "above 20" << endl;
            }
        else
            cout << "above 20" << endl;
    else if(SrandNumber > 50)
        cout << "above 50" << endl;
    else if(SrandNumber > 60)
        cout << "above 60" << endl;
    else
    {
        cout << "under 10" << endl;
    }
    return 0;
}