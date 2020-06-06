#include <iostream>
using namespace std;
int main(){
	int n;
	cin >> n;
	int m1[n], m2[n];
	for(int i = 0; i < n; i++)
		cin >> m1[i] >> m2[i];
	//输入当前买鱼的钱和保存的钱
	int min = 9999999, t = 0;
	for(int i = 0; i < n; i++) {
		if(min > m1[i])
			min = m1[i];
		t = t + min; //上一条鱼
		min = min + m2[i]; //保存
	}
	cout << t << endl;
	return 0;
}