#include <iostream>
#include<algorithm>
#include <fstream>
#include <string>
#include <windows.h>
#include<sstream>
using namespace std;
const int maxn = 1000;

int n, m;
int pre[maxn];
typedef struct node
{
	int a, b;
	double val;
	node() {
		a = 0;
		b = 0;
		val=0;
	}
}point;

point dian[maxn];

bool cmp(point a, point b)
{
	return a.val < b.val;
}

int find(int x)
{
	return x == pre[x] ? x : pre[x] = find(pre[x]);
}

void join(int x, int y)
{
	int a = find(x);
	int b = find(y);
	if (a != b)
	{
		pre[a] = b;
	}
}

void init()
{
	for (int i = 0; i < n; i++)
		pre[i] = i;
}


string UTF8ToGB(const char* str)
{
	string result;
	WCHAR *strSrc;
	LPSTR szRes;

	//获得临时变量的大小
	int i = MultiByteToWideChar(CP_UTF8, 0, str, -1, NULL, 0);
	strSrc = new WCHAR[i + 1];
	MultiByteToWideChar(CP_UTF8, 0, str, -1, strSrc, i);

	//获得临时变量的大小
	i = WideCharToMultiByte(CP_ACP, 0, strSrc, -1, NULL, 0, NULL, NULL);
	szRes = new CHAR[i + 1];
	WideCharToMultiByte(CP_ACP, 0, strSrc, -1, szRes, i, NULL, NULL);

	result = szRes;
	delete[]strSrc;
	delete[]szRes;

	return result;
}

int main(int argc, char *argv[])
{
	ifstream fp("D:\\pycharm\\untitled\\GUI\\测试文件1.txt");
	string str;
	int num1= 0;
	int zong = 0;
	while (!fp.eof()) {
		getline(fp,str);
		if (str.empty())
			continue;
		
		stringstream is(str);
		is >> n;
		is >> m;
		init();
		point* dian = new point[maxn];
		for (int i = 0; i < m; i++) {
			int x, y;
			double z;
			string now;
			getline(fp, now);
			stringstream is1(now);
			is1 >> x; is1 >> y; is1 >> z;
			dian[i].a = x; dian[i].b = y; dian[i].val = z;
		}
		string ans1;
		getline(fp, ans1);
		ans1= UTF8ToGB(ans1.c_str()).c_str();
		double ans_num = 0;
		if (ans1 != "构不成最小生成树")
		{
			stringstream is2(ans1);
			is2 >> ans_num;
		}

		//算法部分
		sort(dian, dian + m, cmp);
		double ans = 0;
		int k = n - 1;
		for (int i = 0; i < m; i++)
		{
			int fx = find(dian[i].a);
			int fy = find(dian[i].b);
			if (fx != fy)
			{
				k--;
				pre[fx] = fy;
				ans += dian[i].val;
			}
		}

		if (k <= 0 && ans_num == ans) {				
			cout  << ans_num<<'\t'<<'\t'<< '\t'<< '\t'<< '\t';
			cout  << ans<<'\t';
			num1++;
			cout << "答案正确" << endl;
		}
		else if(k>0&& ans1 == "构不成最小生成树") {						 
			cout  << ans1<<'\t';
			cout  << "构不成最小生成树"<<'\t' ;
			num1++;
				cout << "答案正确" << endl;
		}
		else {
			cout << ans;
			cout << ans_num ;
			cout << "答案错误" << endl;
		}
		zong++;
	}

	cout << endl<<endl;
	cout << "测试样例总数为: " << zong << endl;
	cout << "正确样例总数为: " << num1 << endl;
	double lv = (double)num1 / zong;
	//cout << endl << "正确率为: " << lv << endl;
	printf("\n正确率为: %.0f%%\n\n", lv * 100.0);

	return 0;
}