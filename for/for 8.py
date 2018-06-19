a,b=map(int,input().split())


for i in range(1,a):

    if i==2:
        b=b+28
    elif i==1 or i==3 or i==5 or i==8 or i==10 or i==7:
        b=b+31
    elif i==4 or i==6 or i==9 or i==11:
        b=b+30

if b%7==0:
    print('SUN')
elif b%7==1:
    print('MON')
elif b%7==2:
    print('TUE')
elif b%7==3:
    print('WED')
elif b%7==4:
    print('THU')
elif b%7==5:
    print('FRI')
elif b%7==6:
    print('SAT')

