import heapq

def astar_all_paths(self, h, start, goal):
	pq = [(h[start], start, [start], 0)]
	found_paths = []
	while pq:
		pri, cur, p, g = heapq.heappop(pq)
		if cur == goal:
			print(f"Path Found: {p} | Total Distance: {g}")
            		found_paths.append((g, p))
            		continue 
        	for n, w in self.adjlist.get(cur, []):
           		if n in p: 
                		continue
			ng = g + w
            		nf = ng + h[n]
                        heapq.heappush(pq, (nf, n, p + [n], ng))
		return found_paths

