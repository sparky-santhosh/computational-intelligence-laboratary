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
	def UCS(self,start,end):
		pq=[(0,start)]
		path={start:None}
		found=False
		cost={start:0}
		p=[]
		while pq:
			#print(list(pq))
			cc,cur=heapq.heappop(pq)
			print("Currently in "+str(cur))
			if cur==end:
				found=True
				break
			for i,w in self.adjlist[cur]:
				nc=cc+w
				if i not in cost or nc<cost[i]:
					print("Expanding "+str(i))
					cost[i]=nc
					path[i]=cur
					heapq.heappush(pq,(nc,i))
		if found:
			way=[]
			t=end
			while t is not None:
				way.append(t)
				t=path[t]
			print("path: "+"-".join(way[: :-1]))
			print("cost: "+str(cost[end]))
	def DFS(self,start,end):
		if start not in self.adjlist:
			print("Start node not present!!")
			return
		visit={start}
		stack=[start]
		p=[]
		path={start:None}
		found=False
		while stack:
			print("fringe : ",stack)
			c=stack.pop()
			p.append(c)
			if c==end:
				found=True
				break
			for (i,z) in self.adjlist[c]:
				if i not in visit:
					print("Currently in ",i)
					visit.add(i)
					path[i]=c
					stack.append(i)
		if found:
			way=[]
			cur=end
			while cur is not None:
				way.append(cur)
				cur=path[cur]
			print("Path = "+"-".join(p))
		else:
			print("Search element not found !!!")
	def BFS(self,start,end):
		visit={start}
		queue=deque([start])
		path={start:None}
		found=False
		p=[]
		print()
		while queue:
			print("fringe ",list(queue))
			c=queue.popleft()
			p.append(c)
			if c==end:
				found=True
				break
			for (i,z) in self.adjlist[c]:
				if i not in visit:
					print("Currently in ",i)
					visit.add(i)
					path[i]=c
					queue.append(i)
		if found:
			way=[]
			cur=end
			while(cur is not None):
				way.append(cur)
				cur=path[cur]
			print("Path = "+"-".join(p))
		else:
			print("Search element cant be reached")
def main():
	g=graph()
	print("\tMENU")
	print("1)add node\n2)remove node\n3)add edge\n4)remove edge\n5)print adjacency list\n6)Breadth First Search\n7)Depth First Search\n8)Uniform Cost Search\n9)Exit")
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
			start=input("Enter the start node: ")
			end=input("Enter the goal node : ")
			g.BFS(start,end)
		elif ch==7:
			start=input("Enter the start node : ")
			end = input("Enter the goal node : ")
			g.DFS(start,end)
		elif ch==8:
			start=input("Enter the start node : ")
			goal=input("Enter the goal node : ")
			g.UCS(start,goal)
		else:
			break		
main()
