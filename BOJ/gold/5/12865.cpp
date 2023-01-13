#include <iostream>
#include <algorithm>

int dp[101][100001];
std::pair<int, int> item[101];
int n, k;

void input() {
	std::cin >> n >> k;
	for (int i = 1; i <= n; i++) {
		std::cin >> item[i].first >> item[i].second;
	}
	std::sort(item, item + n + 1);
}

int cal() {
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			if (item[i].first > j) dp[i][j] = dp[i - 1][j];
			else dp[i][j] = std::max(dp[i - 1][j], dp[i - 1][j - item[i].first] + item[i].second);
		}
	}
	return dp[n][k];
}

int main() {
	input();
	std::cout << cal();
}