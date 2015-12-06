
f=open("outmalt_3_12")
a=f.readlines()
f.close()
count=0

for i in a:
	if i != '\n':
		if (i.split()[3]!="punc" and i.split()[7]=="ROOT"):
			count+=1
print count
