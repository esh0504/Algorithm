num=int(input())
wordList=[]
for i in range(num):
	word=input()
	wordList.append(word)
count=0
for i in range(num):
	useword=[]
	wordList[i]=wordList[i]+'?'
	for k in range(len(wordList[i])-1):
		if wordList[i][k]==wordList[i][k+1]:
			continue
		else:
			if wordList[i][k] in useword:
				count-=1
				break
			else:
				useword.append(wordList[i][k])
	count+=1

print(count)

		
		
