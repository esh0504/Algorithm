#include <iostream>
#include <map>

using namespace std;

map<int, int> sol(map<int, int> m) {
	map<int, int> tmpdic;
	tmpdic.insert(pair<int,int>(0, m[1]));
	tmpdic.insert(pair<int,int>(9, m[8]));
	for (int i = 1; i < 9; i++) {
		tmpdic.insert(pair<int,int>(i, ((m[i - 1])%1000000000 + (m[i + 1])%1000000000)%1000000000));
	}
	return tmpdic;
}

int main() {

	map <int, int> dic;
	dic.insert(pair<int,int>(0, 0));
	for (int i = 1; i < 10; i++) {
		dic.insert(pair<int,int>(i, 1));
	}
	int n;
	cin >> n;
	for (int i = 1; i < n; i++) {
		dic=sol(dic);
	}
	int result = 0;
	for (int i = 0; i < 10; i++) {
		result += dic[i];
		result %= 1000000000;
	}
	cout << result << endl;
}