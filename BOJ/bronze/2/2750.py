num=int(input())
list=[]
for i in range(num):
    a=int(input())
    list.append(a)

list.sort()
for i in range(num):
    print(list[i])
