filename=raw_input("enter filename")
	
f=open(filename)
infile=f.readlines()
f.close()
d={}
counts=0
countw=0
for i in infile:
	if i=='\n':
		counts+=1
		print counts,countw
		if  str(countw) in d.keys():
			d[str(countw)]+=1
		else:
			d[str(countw)]=1
		countw=0

	else:
		countw+=1



print
print d


count10=0
count20=0
count30=0
count40=0
count50=0
for key in d:
	if int(key) <= 10:
		count10+=d[key]
	elif int(key) > 10 and int(key) <= 20:
		count20+=d[key]
	elif int(key) > 20 and int(key) <= 30:
		count30+=d[key]
	elif int(key) > 30:
		count40+=d[key]


print count10,count20,count30,count40
		
