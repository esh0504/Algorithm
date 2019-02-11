testCase=int(input())

for i in range(testCase):
    m,n,k=map(int,input().split())
    Map=[]
    Map2=[]
    ## 밭의 크기 만들기
    for ga in range(n):
        Map2=[]
        for se in range(m):
            Map2.append(0)
        Map.append(Map2)
    
    ## 밭에 벌레 뿌리기 
    for k in range(k):
        x,y=map(int,input().split())
        Map[y][x]=1
   
    ## 배추에서 오른쪽,위를 봐서 배추가 없으면 count+=1
    count=0
    for se in range(n):
        for ga in range(m):
            #중앙일때
            if se!=0 and ga!=m-1:
                if Map[se][ga]==1:
                    if Map[se][ga+1]==1:
                        continue
                    elif Map[se-1][ga]==1:
                        continue
                    else:
                        count+=1
            # 오른쪽이 없을때 (단 세로가 1이상)
            elif ga==m-1 and se!=0:
                if Map[se][ga]==1:
                    if Map[se-1][ga]==1:
                        continue
                   
                    else:
                        count+=1
            # 위가 없을때(맨오른쪽제외)
            elif se==0 and ga!=m-1:
                if Map[se][ga]==1:
                    if Map[se][ga+1]==1:
                        continue
                    else:
                        count+=1
            #맨위맨오른쪽
            elif se==0 and ga==m-1:
                if Map[se][ga]==1:
                    count+=1
    print(count)

        
