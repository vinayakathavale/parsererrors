inp=raw_input("correct filename")
test=raw_input("parser o/p filename")
	
	
f=open(inp)
infile=f.readlines()
f.close()

f=open(test)
outfile=f.readlines()
f.close()
count=0
assert len(infile)==len(outfile)

for i in range(len(infile)):
	if infile[i]!=outfile[i]:
		count+=1
print count
print 1-float(count)/len(outfile)
