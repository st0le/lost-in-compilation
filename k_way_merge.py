import random,heapq

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

arr = []
for i in xrange(3):
    arr.append(sorted(random_array(5)))
    
def merge(arr):
    k = len(arr)
    index = [0] * k
    lst = []
    while True:
        mni = None
        for i in xrange(k):
            if index[i] < len(arr[i]) and (mni == None or arr[i][index[i]] < arr[mni][index[mni]]):
                mni = i
        if mni == None: break
        lst.append(arr[mni][index[mni]])
        index[mni] += 1
    return lst

def merge2(arr):
    heap = [(l[0],i,0) for i,l in enumerate(arr) if len(l) > 0]
    heapq.heapify(heap)
    lst = []
    while heap:
        item,lst_index,item_index = heapq.heappop(heap)
        lst.append(item)
        if item_index + 1 < len(arr[lst_index]):
            heapq.heappush(heap,(arr[lst_index][item_index+1],lst_index,item_index+1))
    return lst

print arr
print merge(arr)
print merge2(arr)