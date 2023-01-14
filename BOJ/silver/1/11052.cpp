#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int n;
	cin >> n;
	int dp[1001];
	int arr[1001];
	for (int i = 1; i <= n; i++) {
		cin >> dp[i];
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1, k = i-1; j <= k; j++, k--) {
			dp[i] = max(dp[j] + dp[k], dp[i]);
		}
	}
	cout << dp[n];
}