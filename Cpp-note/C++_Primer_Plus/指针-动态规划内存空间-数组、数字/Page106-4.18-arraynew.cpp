#include <iostream>

using namespace std;

int main()
{
    double * p3 = new double[3]; //3个元素的数组
	p3[0] = 0.2;
	p3[1] = 0.5;
	p3[2] = 0.8;
	cout << "p3[1] is: " << p3[1] << ".\n";
	p3 += 1;
	cout << "now p3[0] is:"  << p3[0] << endl;
	p3 -= 1;
	delete [] p3;
	
	const int cc = 10;
	int * lib = new int[10];
	delete []lib;
	return 0;
}

