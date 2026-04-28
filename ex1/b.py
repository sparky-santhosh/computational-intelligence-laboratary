from collections import deque

class graph:
	def __init__(self):
		self.adjlist = {}

	def addnode(self, u):
		if u not in self.adjlist:
			self.adjlist[u] = []

	def delnode(self, v):
		if v in self.adjlist:
			for i in self.adjlist[v]:
				self.adjlist[i].remove(v)
			del self.adjlist[v]

	def addedge(self, u, v):
		if u not in self.adjlist: self.addnode(u)
		if v not in self.adjlist: self.addnode(v)
		if v not in self.adjlist[u]:
			self.adjlist[u].append(v)
		if u not in self.adjlist[v]:
			self.adjlist[v].append(u)

	def deledge(self, u, v):
		if u in self.adjlist and v in self.adjlist[u]:
			self.adjlist[u].remove(v)
			self.adjlist[v].remove(u)

	def printlist(self):
		for i, j in self.adjlist.items():
			# Convert list j to string to allow concatenation
			print(i + " : " + str(j))

	def BFS(self, start, end):
		if start not in self.adjlist or end not in self.adjlist:
			print("Search element cant be reached")
			return
		
		visit = {start}
		queue = deque([start])
		path = {start: None}
		found = False
		
		while queue:
			c = queue.popleft()
			if c == end:
				found = True
				break
			for i in self.adjlist[c]:
				if i not in visit:
					visit.add(i)
					path[i] = c
					queue.append(i)

		if found:
			way = []
			cur = end
			while(cur is not None):
				way.append(cur)
				cur = path[cur]
			# Iterate backwards and use end="" to stay on the same line
			for i in range(len(way)-1, -1, -1):
				print(str(way[i]) + "-", end="")
			print() # New line after finishing the path
		else:
			print("Search element cant be reached")

def main():
	g = graph()
	print("\tMENU")
	print("1)add node\n2)remove node\n3)add edge\n4)remove edge\n5)print adjacency list 6)Breadth First Search 7)exit")
	while True:
		ch = int(input("Enter your choice : "))
		if ch == 1:
			e = input("Enter the name of new node : ")
			g.addnode(e)
		elif ch == 2:
			e = input("Enter the node to be deleted : ")
			g.delnode(e)
		elif ch == 3:
			e = input("enter node 1: ")
			f = input("enter node 2: ")
			g.addedge(e, f)
		elif ch == 4:
			e = input("Enter node 1: ")
			f = input("Enter node 2: ")
			g.deledge(e, f)
		elif ch == 5:
			print("Adjacency list : ")
			g.printlist()
		elif ch == 6:
			s = input("Start node: ")
			e = input("End node: ")
			g.BFS(s, e)
		else:
			break

if __name__ == "__main__":
	main()

