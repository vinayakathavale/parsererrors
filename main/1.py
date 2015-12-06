f=open("intest_3_12")
infile=f.readlines()
f.close()

f=open("outmalt_3_12")
outfile=f.readlines()
f.close()
count=0
assert len(infile)==len(outfile)

for i in range(len(infile)):
	if infile[i]!=outfile[i]:
		count+=1
print count
print 1-float(count)/len(outfile)
