#include <cstdio>
int main() {
	int t, m, n, x, y;
	int mul;
	scanf("%d", &t);
	for (int i = 0; i<t; i++) {
		scanf("%d%d%d%d", &m, &n, &x, &y);
		mul = m*n;
		while (x != y && x <= mul)
		{
			if (x < y)
				x += m;
			else
				y += n;
		}
		if (x != y)
			printf("-1\n");
		else
			printf("%d\n", x);
	}
}

