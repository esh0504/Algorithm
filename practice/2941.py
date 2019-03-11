a=input()

b=["c=","c-","dz=","d-","lj","nj","s=","z="]
count=0
while len(a)!=0:

	for i in b:
		if a[:len(i)] in b:
			count+=1
			a=a[len(i):]
		else:
			count+=1
			a=a[1:]

print(count)

