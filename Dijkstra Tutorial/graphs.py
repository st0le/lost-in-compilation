import pqueue

def dijkstra(graph,src,dst):
	min_dist = dict()        # stores shortest path from src, ie min_dist[u] = w denotes, weight of shortest path (src->u) = w
	prev_vertex = dict()	 # prev_vertex[u], stores the previous node on the shortest path from src to u
	pq = pqueue.pqueue()
	pq.push( (0, src) )
	min_dist[src] = 0        # distance to source is 0. 
	prev_vertex[src] = None  # no previous node for src
	while not pq.empty():
		(dist , u ) = pq.pop()
		for (v,w) in graph[u]: #v is adjacent to u, edge weight is w
			if v not in min_dist or w + min_dist[u] < min_dist[v]: # shortest path to v is greater than going through u then v?
				min_dist[v] = w + min_dist[u] # make it the new path
				prev_vertex[v] = u
				pq.push( (min_dist[v], v) )
	
	if dst not in min_dist: #no path from src to dst
		return None,None
	else:
		path = []
		node = dst
		while node:
			path.append(node)
			node = prev_vertex[node]
		path.reverse()
		return min_dist[dst], path #return cost, path