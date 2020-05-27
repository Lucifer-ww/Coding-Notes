#include <iostream>
#include <vector>
#include <string>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <stdlib.h>
#define contrlccc 100039223
#define MAXN 1000001

#define ConstHelpMain "主界面：密码管理   版本1.2.2\n使用方法如下\n1、add：添加密码\n实例：\n>>>add\n输入用户名：Thomas\n输入密码：password123\n提示信息：QQ\n录入完成！\n-----------------\n\
2、help：呼出此页面\n3、exit：退出\n4、show：显示所有记录\n5、cls/clear：清屏\n6、delete：删除某项\n实例：\n>>> delete\n输入你要删除的编号：2\n删除完成！\n-----------------\n按下任意键继续......\n"


#define ConstHelpInline ""
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;
int cnt = 0;
int allcnt; //总计数
typedef struct ctler{
	int id;
	/*string account;
	string pass;
	string info;*/
	char* account;
	char* pass;
	char* info;
	bool flag = true;
}passctl;
passctl cc[MAXN];
class method{
private:
	void clears()
	{
		system("cls");
	}
public:
	method()
	{
		ifstream fin("data/allcnt.txt");
		fin >> allcnt;
	}
	void add()
	{
		string ac, password;
		char ifo[101];
		char cca[101], ccap[101];
		//printf("输入用户名：");
		cout << "输入用户名：";
		//getline(cin, ac);
		//gets(cca);
		scanf("%s", &cca);
		printf("输入密码：");
		//getline(cin, password, '\n');
		//gets(ccap);
		scanf("%s", &ccap);
		printf("信息：");
		//getline(cin, info);
		//gets(ifo);
		scanf("%s", &ifo);
		cc[cnt].id = cnt;
		cc[cnt].account = cca;
		cc[cnt].pass = ccap;
		cc[cnt].info = ifo;
		cnt++;
		allcnt++;
		printf("录入完成！\n");
		ofstream fout("data/save.csv", ios::app);
		fout << cc[cnt].id << "," << cc[cnt].account << "," << cc[cnt].pass << "," << cc[cnt].info << endl; 
		printf("success...\n");
	}
	void help()
	{
		printf(ConstHelpMain);
	}
	void show()
	{
		ifstream fin("data/save.csv"); 
		for (int i = 0; i < allcnt; i++)
		{
			if (cc[i].flag) {
				string tmps;
				getline(fin, tmps);
				for (int i = 0; i < tmps.size(); i++)
				{
					if (tmps[i] == ',') {
						cout << " ";
						continue;
					}
					else{
						cout << tmps[i];
					}
				}printf("\n");
			} else {
				continue;
			}
		}
	}
	void del()
	{
		printf("输入你要删除的编号> ");
		int idx;
		cin >> idx;
		cc[idx - 1].flag = false; //标记法删除模式
		printf("删除成功！\n");
		return;
	}
	void change(int idx, char* account, char* pass, char* info)
	{
		return;
	}
	void clsc()
	{
		clears();
	}
	void gexit()
	{
		ofstream fout("data/allcnt.txt");
		fout << allcnt << endl;
		exit(1);
	}
};
method met;
int main(int argc, char** argv) {
	system("cls");//初始化清空
	printf(ConstHelpMain);
	char tmpj = getch();
	system("cls");
	//delete search cls/clear  回车自动补全 
	//reset/restart
	// change
	#if 1
	while (true)
	{
		printf(">>> ");
		string cp;
		#if 0
		cin >> cp;
		#endif
		getline(cin, cp, '\n');
		if (cp == "add")
			met.add();
		else if (cp == "help")
			met.help();
		else if (cp == "exit")
			met.gexit();
		else if (cp == "show")
			met.show();
		else if (cp == "cls") met.clsc();
		else if (cp == "delete") met.del();
		else if (cp == "clear") met.clsc();
		else if (cp == "");
		else
			printf("语法错误\n");
	}
	#endif
	#if 0
	do{
		printf(">>> ");
		string cp;
		cin >> cp;
		if (cp == "add") met.add();
		else if (cp == "help") met.help();
		else if (cp == "exit") exit(1);
		else if (cp == "show") met.show();
		else if (cp == "\n") printf(">>> ");
		else printf("语法错误\n");
	} while (true);
	#endif
	#if 0
	system("pause");
	#endif
	return 0;
}



//protect:
/*
(const char [306])"主界面：密码管理   版本1.2.2\n使用方法如下\n1、add：添加密码\n实例：\n>>>add\n输入用户名：Thomas\n输入密码：password123\n提示信息：QQ\n录入完成！\n-----------------\n2、help：呼出此页面\n3、exit：退出\n4、show：显示所有记录\n按下任意键继续......\n"
*/