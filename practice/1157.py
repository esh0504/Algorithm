word=input()
wordList=[]

wordList.sort()
if word[0]!=word[1]:
			wordDic={word[0]:1}
			wordList.append(wordDic)
count=1
for i in range(1,len(word)):
	
	if word[i-1]!=word[i]:
		wordDic={word[i]:count}
		wordList.append(wordDic)
		count=1
	else:
		count+=1
		
print(wordList)