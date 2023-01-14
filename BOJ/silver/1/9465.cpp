#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int d[2][100001], arr[2][1000001], n, T;

int main() {
	cin >> T;
	while(T--) {
		cin >> n;
		for (int i = 0; i < 2; ++i) {
			for (int j = 1; j <= n; ++j) {
				cin >> arr[i][j];
			}
		}
		d[0][1] = arr[0][1], d[1][1] = arr[1][1];

		for (int i = 2; i <= n; ++i) {
			d[0][i] = max(d[1][i - 1], d[1][i - 2]) + arr[0][i];
			d[1][i] = max(d[0][i - 1], d[0][i - 2]) + arr[1][i];
		}
		cout << max(d[0][n], d[1][n]) << endl;
	}
}