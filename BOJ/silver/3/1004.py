TestCase=int(input())#테스트케이스

for i in range(TestCase):#반복횟수
    x1,y1,x2,y2=map(int,input().split())#출발점과 도착점
    number_planet=int(input())#행성계의 갯수

    count=0 #답
    x=[]
    y=[]
    r=[]

    for k in range(number_planet):#행성 좌표와 반지름 추가
        a,b,c=map(int,input().split())
        x.append(a)
        y.append(b)
        r.append(c)

    for t in range(number_planet):
        if (x[t]-x1)**2+(y[t]-y1)**2>(x[t]-x2)**2+(y[t]-y2)**2:
            d2=(x[t] - x1) ** 2 + (y[t] - y1) ** 2
            d1=(x[t]-x2)**2+(y[t]-y2)**2
            if d1<r[t]**2 and d2>r[t]**2:
                count+=1

        elif (x[t]-x1)**2+(y[t]-y1)**2<(x[t]-x2)**2+(y[t]-y2)**2:
            d1=(x[t]-x1)**2+(y[t]-y1)**2
            d2=(x[t]-x2)**2+(y[t]-y2)**2
            if d1<r[t]**2 and d2>r[t]**2:
                count+=1

    print(count)