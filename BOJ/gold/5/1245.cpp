#include <iostream>
#include <stack>
using namespace std;

int row, col;
int answer = 0;
bool isBonguri = true;
//상하좌우 방향 + 대각선
pair <int, int> dir[8] = { make_pair(-1,0),make_pair(1,0),make_pair(0,-1),make_pair(0,1), make_pair(1,1), make_pair(1,-1),make_pair(-1,1),make_pair(-1,-1)};

int map[101][71] = {0};
bool visitCheck[101][71] = { false };

bool bonguriCheck(int y, int x, int bong) {
	return map[y][x] <= bong;
}

void DFS(int y, int x) {

	for (int i = 0; i < 8; i++) {
		int nextX = x + dir[i].second;
		int nextY = y + dir[i].first;
		if (nextX < 0 || nextY < 0 || nextY > row || nextX > col) continue;
		if (!bonguriCheck(nextY, nextX, map[y][x])){
			isBonguri = false;
		}
		if (visitCheck[nextY][nextX] || map[y][x] != map[nextY][nextX])continue;
		visitCheck[nextY][nextX] = true;
		DFS(nextY, nextX);
	}
}

int main(void) {
	cin >> row >> col;
	for (int i = 1; i <= row; i++) {
		for (int j = 1; j <= col; j++) {
			cin >> map[i][j];
		}
	}
	for (int i = 1; i <= row; i++) {
		for (int j = 1; j <= col; j++) {
			if (!visitCheck[i][j]) {
				isBonguri = true;
				DFS(i, j);
				if (isBonguri) {
					answer++;
				}

			}
		}
	}
	cout << answer << endl;
	return 0;
}