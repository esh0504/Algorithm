import operator
stats=[]

num=int(input())
for i in range(num):
	str,intell,stat=map(int,input().split())
	dir={'str':str,'int':intell,'stat':stat}
	stats.append(dir)

strdir=sorted(stats,key=operator.itemgetter('str'))
intdir=sorted(stats,key=operator.itemgetter('int'))

strsum=1
intellsum=1

for i in range(num):
	if strsum>=strdir[i]['str']:
		
		strsum+=strdir[i]['stat']
		if i==num-1:
			a=i+1
	else:
		a=i
		break

for i in range(num):
	if intellsum>=intdir[i]['int']:
		intellsum+=intdir[i]['stat']
		if i==num-1:
			b=i+1
	else:
		b=i
		break


if a>b:
	print(a)
else:
	print(b)

