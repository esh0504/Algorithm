#include <stdio.h>

int th(num) {
	return int(num/1000)
}
int hun(num) {
	return int(num/100)
}
int dec(num) {
	return int(num/10)
}
int ill(num) {
	return int(num)
}
int self(num) {
	if (num >= 1000) {
		return num+th(num)+hun(num-(1000*th(num)))+dec(num-(1000*th(num))- hun(num - (1000 * th(num))))+ill(num- (th(num)*1000)-(100*hun(num - (1000 * th(num))))-dec(num - (1000 * th(num)) - hun(num - (1000 * th(num)))))
	}
	else if (num >= 100) {
		return num+hun(num)+dec(num-(100*hun(100)))+ill(num-(hun(num)*100)- dec(num - (100 * hun(100))))
		}
	else if (num >= 10) {
		return num+dec(num)+ill(num-(10*dec(num)))
	}
	else {
		return num
	}
}

int main(void) {
	int list[10000]; 
	for (int i = 0; i < 10000; i++) {
		list[i]=self(i)
	}
	printf(list)

}