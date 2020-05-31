#include <iostream>
#include <string>
using namespace std;
class obj
{
	public:
		string name;
		int age;
};
class Student : obj
{
	public:
		int student_number;
        void printname()
        {
            cin >> name; //private继承，在类中可用
            cout << name << endl;
        }
};
int main()
{
   Student sss;/*
	cin >> sss.name;
	cout << sss.name << endl;*/
    cin >> sss.student_number;
    cout << sss.student_number << endl;
    sss.printname();
   return 0;
}