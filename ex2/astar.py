from collections import deque
import heapq
class graph:
	def __init__(self):
		self.adjlist={}
	def addnode(self,u):
		if u not in self.adjlist:
			self.adjlist[u]=[]
	def delnode(self,v):
		if v in self.adjlist:
			for i in self.adjlist[v]:
				self.adjlist[i].remove(v)
			del self.adjlist[v]
	def addedge(self,u,v,weight=1):
		self.addnode(u)
		self.addnode(v)
		if v not in self.adjlist[u]:
			self.adjlist[u].append((v,weight))
		if u not in self.adjlist[v]:
			self.adjlist[v].append((u,weight))
	def deledge(self,u,v):
	   	if v in self.adjlist[u]:
		   	self.adjlist[u].remove(v)
		   	self.adjlist[v].remove(u)
	def printlist(self):
		for i,j in self.adjlist.items():
			print(str(i)+" : "+str(j))
	def astar(self,h,start,goal):
		pq=[(h[start],start,[start],0)]
		visit={}
		minp=[]
		ming=9999
		while pq:
			pri,cur,p,g=heapq.heappop(pq)
			print("Currently in : "+cur)
			if cur==goal:
				print("Final goal reached ")
				print("Path : ",p)
				print("Distance :",g)
				if g<ming:
					ming=g
					minp=p.copy()
			if cur in visit and visit[cur]<=g:
				continue
			visit[cur]=g
			print("Expanding "+cur+" with neighbours : ",end="")
			for n,w in self.adjlist[cur]:
				#print(n,end=",")
				if n in p:
					continue
				ng=g+w
				nf=ng+h[n]
				print(n+" f(n)= ",nf)
				heapq.heappush(pq,(nf,n,p+[n],ng))
			print()
		print("Final Path = ",minp)
		print("With cost = ",ming)
def main():
	g=graph()
	print("\tMENU")
	print("1)add node\n2)remove node\n3)add edge\n4)remove edge\n5)print adjacency list\n6)A Star Search \n7)Exit")
	while True:
		ch=int(input("Enter your choice : "))
		if ch==1:
			e=input("Enter the name of new node : ")
			g.addnode(e)
		elif ch==2:
			e=input("Enter the node to be deleted : ")
			g.delnode(e)
		elif ch==3:
			e=input("enter the source edge : ")
			f=input("Enter the destination edge : ")
			w=int(input("Enter the path cost : "))
			g.addedge(e,f,w)
		elif ch==4:
			e=input("Enter the source edge to delete : ")
			f=input("Enter the destination edge : ")
			g.deledge(e,f)
		elif ch==5:
			print("Adjacency list : ")
			g.printlist()
		elif ch==6:
			s=input("Enter the start node : ")
			h=dict()
			goal=input("Enter the goal node : ")
			for i in g.adjlist.keys():
				h[i]=int(input("Enter the hueristics value for "+i))
			h[s]=0
			g.astar(h,s,goal)
		else:
			break		
main()
