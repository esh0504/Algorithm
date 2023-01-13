#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int money[21];
int people[21];
int dp[1101];

int main() {
    for (int i = 0; i < 1101; i++) {
        dp[i] = 999999999;
    }
    dp[0] = 0;

    int cost, cityNum;
    cin >> cost >> cityNum;

    for (int cn = 0; cn < cityNum; cn++) {
        cin >> money[cn] >> people[cn];
        dp[people[cn]] = min(dp[people[cn]],dp[money[cn]]);
    }


    for (int i = 1; i < 1101; i++) {
        for (int cn = 0; cn < cityNum; cn++) {
            if (i - people[cn] >= 0) {
                dp[i] = min(dp[i],dp[i - people[cn]] + money[cn]);
            }
        }
    }

    int shortest = INT_MAX;
    for (int i = cost; i < 1101; i++) {
        shortest = min(shortest, dp[i]);
    }

    cout << shortest;
}