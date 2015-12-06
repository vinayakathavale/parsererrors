f=open("intest_3_12")
infile=f.readlines()
f.close()

startsentence=0
countw=0
count=0
for i in range(len(infile)):
	if infile[i] == '\n':
		if countw <= 10:
			f=open("10inp","a")
		if countw > 10 and countw <= 20:
			f=open("20inp","a")
		if countw > 20 and countw <= 30:
			f=open("30inp","a")
		if countw > 30:
			f=open("40inp","a")
		
		for j in range(startsentence,i):
			f.write(infile[j])
		f.write('\n')
		f.close()
			
		countw=0 
		startsentence=i+1
	else:
		countw+=1
		count+=1


