#include <iostream>
#include <map>

using namespace std;

#define endl '\n'

// Set up : Global Variables
map<char,int> V;

// Set up : Functions Declaration
int decoder(string r);
string encoder(int val);


int main()
{
    // Set up : I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // Process
    /* 로마숫자값 Map 에 저장 */
    V['I'] = 1;
    V['V'] = 5;
    V['X'] = 10;
    V['L'] = 50;
    V['C'] = 100;
    V['D'] = 500;
    V['M'] = 1000;

    // Set up : Input
    string r1, r2;
    cin >> r1 >> r2;

    // Process
    int a1 = decoder(r1);
    int a2 = decoder(r2);

    // Control : Output
    cout << a1+a2 << endl;
    cout << encoder(a1+a2) << endl;
}

// Helper Functions
int decoder(string r)
/* 주어진 로마 숫자에 해당하는 아라비아 숫자를 반환 */
{
    int val = 0;
    for (int i=0; i<r.length(); i++) {
        val += V[r[i]]; /* 마주치는 로마 숫자의 숫자값을 더함 */
        /* 이전의 로마숫자값이 현재의 로마숫자값보다 작으면 */
        if (i > 0 && V[r[i-1]] < V[r[i]]) {
            val -= 2*V[r[i-1]]; /* IV, IX, XL, XC, CD, CM 과 같은 예외에 해당
                                 * 이전의 로마숫자값이 더해진 상태이므로, 그 값을 2번 빼줌 */
        }
    }

    return val;
}

string encoder(int val)
/* 주어진 아라비아 숫자에 해당하는 로마 숫자를 반환 */
{
    string rome;

    /* 천의 자리 */
    int d4 = val / 1000; /* 천의 자리수 */
    val %= 1000;
    /* d4 는 0~3 의 값을 가질 수 있음
     * IV, IX, XL, XC, CD, CM 과 같은 예외도 없음
     * 그냥 d4 만큼 'M' 추가 */
    for (int i=0; i<d4; i++) {
        rome.push_back('M');
    }

    /* 백의 자리 */
    int d3 = val / 100; /* 백의 자리수 */
    val %= 100;
    if (d3 == 4 || d3 == 9) { /* CD, CM 예외 처리 */
        rome.push_back('C');
        if (d3 == 4) { rome.push_back('D'); }
        if (d3 == 9) { rome.push_back('M'); }
    } else {
        if (d3 >= 5) { rome.push_back('D'); d3 -= 5; } /* D 처리 */
        for (int i=0; i<d3; i++) { /* 남은 d3 만큼 'C' 추가 */
            rome.push_back('C');
        }
    }

    /* 십의 자리 */
    int d2 = val / 10; /* 십의 자리수 */
    val %= 10;
    if (d2 == 4 || d2 == 9) { /* XL, XC 예외 처리 */
        rome.push_back('X');
        if (d2 == 4) { rome.push_back('L'); }
        if (d2 == 9) { rome.push_back('C'); }
    } else {
        if (d2 >= 5) { rome.push_back('L'); d2 -= 5; } /* L 처리 */
        for (int i=0; i<d2; i++) { /* 남은 d2 만큼 'X' 추가 */
            rome.push_back('X');
        }
    }

    /* 일의 자리 */
    int d1 = val; /* 일의 자리수 */
    if (d1 == 4 || d1 == 9) { /* IV, IX 예외 처리 */
        rome.push_back('I');
        if (d1 == 4) { rome.push_back('V'); };
        if (d1 == 9) { rome.push_back('X'); }
    } else {
        if (d1 >= 5) { rome.push_back('V'); d1 -= 5; } /* V 처리 */
        for (int i=0; i<d1; i++) { /* 남은 d1 만큼 'I' 추가 */
            rome.push_back('I');
        }
    }

    return rome;
}