testCase=int(input())
for i in range(testCase):
    a=input()
    sum=0
    score=0
    for k in range(len(a)):
        if a[k]=="O":
            score+=1
            sum+=score
        else:
            score=0
    print(sum)
