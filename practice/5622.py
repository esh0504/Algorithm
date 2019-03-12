a=input()
answer=0
ls=[["A","B","C"],["D","E","F"],["G","H","I"],["J","K","L"],["M","N","O"],["P","Q","R","S"],["T","U","V"],["W","X","Y","Z"]]
for i in range(len(a)):
    for k in ls:
        if a[i] in k:
            answer+=ls.index(k)+3
print(answer)