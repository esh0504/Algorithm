a = input()
b = input()
if int(a)<int(b):
    a ,b = b,a
at =len(a)
bt = len(b)
e =0
re =10**5
for i in range(len(a)):
    c = 0
    t=0
    for j in range(len(b)):
        try:
            if a[i+j] == '2' and b[j]=='2':
                t=1
                break
            else:
                c+=1
        except:
            break
    if c == bt:
        e =1
        re =min(re,at)
        break
    if t==0:
        re = min(re,at+len(b)-c)

e=0
for i in range(len(b)):
    c = 0
    t=0
    for j in range(len(a)):
        try:
            if b[i+j] == '2' and a[j]=='2':
                t=1
                break
            else:
                c+=1
        except:
            break
    if c == bt:
        e =1
        re =min(re,at)
        break
    if t==0:
        re = min(re,bt+len(a)-c)

if re==10**5:
    print(bt+at)
else:
    print(re)