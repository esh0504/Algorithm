page=int(input())
quest=input()
count=0
questlist=quest.split()
i=0
for i in range(page):
    questlist[i]=int(questlist[i])

i=0
while (i<page):
    if i==0:
        check=questlist[i]
    else:

        check=questlist[i-1]
    if i==check-1:
        count+=1
        i+=1
        continue
    
    else:
        i+=1
        if check>questlist[i]:
            i+=1
            continue
        else:
            check=questlist[i]
            i+=1
            continue
print(count)