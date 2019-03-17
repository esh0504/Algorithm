word=input()
wordOrd=[]
for i in range(len(word)):
    if ord(word[i])>=97:
        wordOrd.append(ord(word[i])-32)
    else:
        wordOrd.append(ord(word[i]))
wordOrd.sort()
count=0
count2=1
answer=word[0]
wordOrd.append(10000)
for i in range(len(wordOrd)-1):
    wordOrd[i]=chr(wordOrd[i])

for i in range(len(word)):

    if wordOrd[i]==wordOrd[i+1]:
        count2+=1
    else:
        if count>count2:
            count2=1
        elif count==count2:
            count2=1
            answer='?'
        else:
            count=count2
            count2=1
            answer=wordOrd[i]

print(answer)