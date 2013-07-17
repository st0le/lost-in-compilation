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
	
def reverse_graph(g):
	rg = dict()
	for u in g:
		rg[u] = list()
	for u in g:
		for v,w in g[u]:
			rg[v].append((u,w))
	return rg		
	

def bidirectional_dijkstra(g,src,dst,undirected):
	rg = g if undirected else reverse_graph(g) #if graph is directed, prepare reverse graph for BI
	
	#data structures for FI
	pq_fi = pqueue.pqueue()
	prev_fi = dict()
	min_dist_fi = dict()
	
	#data structures for BI
	pq_bi = pqueue.pqueue()
	prev_bi = dict()
	min_dist_bi = dict()

	#initialize FI
	processed_fi = set()
	prev_fi[src] = None
	min_dist_fi[src] = 0
	pq_fi.push((min_dist_fi[src], src))

	#initialize BI
	processed_bi = set()
	prev_bi[dst] = None
	min_dist_bi[dst] = 0
	pq_bi.push((min_dist_bi[dst], dst))

	while not pq_fi.empty() and not pq_bi.empty():
		d,u = pq_fi.pop()
		
		processed_fi.add(u)
		if u in processed_bi: break
		
		for v,w in g[u]:
			if v not in min_dist_fi or w + min_dist_fi[u] < min_dist_fi[v]:
				t = min_dist_fi[v] = w + min_dist_fi[u]
				prev_fi[v] = u
				pq_fi.push( (t , v) )
				
		d,u = pq_bi.pop()
		
		processed_bi.add(u)
		if u in processed_fi: break
		
		for v,w in rg[u]:
			if v not in min_dist_bi or w + min_dist_bi[u] < min_dist_bi[v]:
				t = min_dist_bi[v] = w + min_dist_bi[u]
				prev_bi[v] = u
				pq_bi.push( (t , v) )
	
	#find intermediate node
	k = None
	path_cost = None
	for k_ in min_dist_fi:
		if k_ in min_dist_bi:
			cost = min_dist_fi[k_] + min_dist_bi[k_]
			if path_cost == None or path_cost > cost :
				path_cost = cost
				k = k_

	#no shortest path
	if k == None:
		return None,None

	path = []
	#build path from k to source
	node = k
	while node != None:
		path.append(node)
		node = prev_fi[node]
	path.reverse() #reverse it so it's source->k
	node = prev_bi[k] # skip k, we already inserted it
	#build path from k to dst
	while node != None:
		path.append(node)
		node = prev_bi[node]
	
	return path_cost,path