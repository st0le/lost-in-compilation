import sys,graphs,itertools

def prepare_graph():
    diff_by_1 = lambda (x,y): len(x) == len(y) and sum(1 for a,b in zip(x,y) if a != b) == 1
    graph = {}
    for x,y in filter(diff_by_1,itertools.product(words,repeat=2)):
        if x not in graph: graph[x] = []
        if y not in graph: graph[y] = []
        graph[x].append( ( y , 1) )
        graph[y].append( ( x , 1) )
    return graph

if __name__ == '__main__':
    if len(sys.argv) >= 3 and  len(sys.argv[1]) == len(sys.argv[2]):
        src,dst = sys.argv[1:]
        words = filter(lambda w : len(w) == len(src), sys.stdin.read().split()) #only consider those words with same length as parameter
        if src in words and dst in words:
            print graphs.dijkstra(prepare_graph(),src,dst)
        else:
            print "Both words should be present in the dictionary."
    else:
        print "Missing command line parameters."