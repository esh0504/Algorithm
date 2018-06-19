num=[]
nonself=[]
for i in range(1,10001):
    num.append(i)
for t in range(10000):
    if t<9:
        nonself.append(num[t])
    elif t<99:
        nonself.append(num[t]+int(num[t]/10)+int(num[t]-int(num[t]/10)))
    elif t<999:
        nonself.append(num[t]+int(num[t]/100)+int((num[t]-int(num[t]/100))/10)+int(num[t]-int(num[t]/100)-int((num[t]-int(num[t]/100))/10)))
    elif t<9999:
        nonself.append(num[t]+int(num[t]/1000)+int((num[t]-int(num[t]/1000))/100)+int((num[t]-int(num[t]/1000)-int((num[t]-int(num[t]/1000))/100)/10))+int(num[t]-int(num[t]/1000)-int((num[t]-int(num[t]/1000))/100)-int((num[t]-int(num[t]/1000)-int((num[t]-int(num[t]/1000))/100)/10))))

for k in range(len(nonself)):
    print(nonself[k],end=" ")




