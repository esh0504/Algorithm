testCase=int(input())
for i in range(testCase):
    R,S=map(str,input().split())
    R=int(R)
    result=""
    for k in range(len(S)):
        result+=S[k]*R
    print(result)

