inp=raw_input("enter correct filename")
inp2=raw_input("enter parser op")

depth=input("enter depth")

f=open(inp)
a=f.readlines()
f.close()

f=open(inp2)
b=f.readlines()
f.close()

CC=0
Ccount=0

startsentence=0
for i in range(len(a)):
	if a[i] == '\n':
		assert(b[i]=='\n')

		list1=[]
		start=-1
		for j in range(startsentence,i):
			if "0	main" in a[j]:
				start= j-startsentence
		assert(start >= 0)

		tempdepth=depth	
		lala=0
		list1.append(a[start+startsentence])

		while tempdepth > 0:
			tempdepth-=1
			for j in range(startsentence,i):
				for k in list1:	
					if k.split()[0] == a[j].split()[6]:
						if a[j] not in list1:
							list1.append(a[j])


		list2=[]
		start=-1
		for j in range(startsentence,i):
			if "0	main" in b[j] or "ROOT" in b[j]:
				start= j-startsentence


		assert(start >= 0)

		tempdepth=depth	
		lala=0
		list2.append(b[start+startsentence])
		
		while tempdepth > 0:
			tempdepth-=1
			for j in range(startsentence,i):
				for k in list2:	
#			print list2
					if k.split()[0] == b[j].split()[6]:
						if b[j] not in list2 and b[j]!='\n':
							list2.append(b[j])


		for l in list1:
			if l in list2:
				Ccount+=1
				
		CC+=len(list1)


		startsentence=i+1


print Ccount
print CC
print Ccount/float(CC)
