import fileinput,graphs
 
# add_edge (u -> v) with weight w to graph
def add_edge(graph,u,v,w):
        if u in graph:                  #vertex u already in graph?
		l = graph[u]            #get list of neighbours
	else:
		graph[u] = l = list()	#insert u into graph and assign an empty list of neighbours
	l.append((v,w))                 #append tuple (v,w) into the neighbour list
	
 
g = dict()                              #initialize graph
for line in fileinput.input():
	u,v,w = map(int,line.split())
	add_edge(g,u,v,w)
	add_edge(g,v,u,w)               #undirected graph, edges go both ways
	
print graphs.dijkstra(g,1,5)        #from wikipedia