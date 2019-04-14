from operator import itemgetter
def distance(x, y):
    return ((x**2)+(y**2))**0.5

testCase=int(input())
for i in range(testCase):
    num=int(input())
    jwa=[]
    xsum=0
    xsum2=0
    ysum2=0
    ysum=0
    for k in range(num):
        x,y=map(int,input().split())
        dic1={'x':x,'y':y,'distance':distance(x,y)}
        jwa.append(dic1)
    jwa=sorted(jwa,key=itemgetter('distance'))
    for h in range(0,num,2):
        xsum+=jwa[h]['x']
        ysum+=jwa[h]['y']
        xsum2+=jwa[h+1]['x']
        ysum2+=jwa[h+1]['y']
    if distance(xsum2,ysum2)>distance(xsum,ysum):
        xresult=xsum-xsum2
        yresult=ysum-ysum2
    else:
        xresult=xsum2-xsum
        yresult=ysum2-ysum
    print(distance(xresult,yresult))