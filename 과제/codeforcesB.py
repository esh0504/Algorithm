testCase=int(input())
wordCopy=[]
wordCopy2=[]
        
for i in range(testCase):
    word=input()
    for k in range(len(word)):
        wordCopy.append(ord(word[k]))
    wordCopy.sort()
    while(len(wordCopy)==len(word)):
        for ij in range(len(word)):
            
            wordCopy2.append(wordCopy[ij])
            for p in range(len(word)):
                if p==ij:
                    continue
                if wordCopy[p]-wordCopy2[len(wordCopy)-1]==1 or wordCopy[p]-wordCopy2[len(wordCopy)-1]==-1:
                    continue
                else:
                    wordCopy2.append(wordCopy[p])


    print(wordCopy)

    