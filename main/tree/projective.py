class Tree(object):
	
	leavee=0

	def __init__(self,name,children=None):
		self.name=name
		self.children=[]
		self.visited=0
		self.discovery=0
		self.leave=0

	def addChild(self,node):
		self.children.append(node)

	def dfs(self,vis):
		Tree.leavee+=1
		self.visited=1
		self.discovery=vis

		if len(self.children)==0:
			self.leave=vis+1
			Tree.leavee+=1

		for i in range(len(self.children)):
			self.children[i].dfs(vis+1)
			Tree.leavee+=1
			if i==len(self.children)-1:
				self.leave=Tree.leavee

	def printTree(self):
		print self.name
		for i in self.children:
			i.printTree()


def buildtree(a,start,end):
	head=-1
	for i in range(start,end):
#print i
		if "0	main" in a[i]:
			head=i+1

	assert (head > 0)

	ll=[]
	for i in range(1,end-start+1):      #created  node
		temp=Tree(i)
		ll.append(temp)

	for i in range(start,end):         #created tree
		p=int(a[i].split()[6])
		c=int(a[i].split()[0])
#	print p, c
		if p>0:		      
			ll[p-1].addChild(ll[c-1])

	assert (head > 0)
	
	print head
	ll[head-start-1].dfs(1)      

	pro=[]
#	print ll[p].discovery


	for i in range(end-start):
		p=a[i+start].split()[6]
		c=a[i+start].split()[0]

		temp=int(p)
		temp1=int(c)
		if(p>c):
			temp1=int(p)
			temp=int(c)

		count=0	

		for j in range(temp+1,temp1-1):
			if (ll[j].discovery < ll[int(p)-1].discovery):  (ll[j].leave > ll[int(p)-1].leave):
				count+=1
				if count==1:
					pro.append(start+j)
					
		

	ll=[]
	return pro 



inp=raw_input("enter correct ")
inp2=raw_input("enter parser ")


f=open(inp)
a=f.readlines()
f.close()

f=open(inp2)
b=f.readlines()
f.close()



startsent=0
count=0
c=0
for i in range(len(a)):
	if a[i]=='\n':
		pro=[]
		pro=buildtree(a,startsent,i)

		if len(pro) > 0:
			count+=1

	
		print "a"		

		c+=1

		startsent=i+1

print
print count
print c
