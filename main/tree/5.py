inp=raw_input("enter correct ")
inp2=raw_input("enter parser ")


f=open(inp)
a=f.readlines()
f.close()

f=open(inp2)
b=f.readlines()
f.close()

startsent=0
for i in range(len(a)):
	if a[i]=='\n':
		buildtree(a,startsent,i)
		




		startsent=i+1




def buildtree(a,start,end):

