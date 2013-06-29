
# Time Complexity : O(n), Query O(1)
# Space Complexity : O(n)
def min_array_6(arr):
    N = len(arr)
    #Cartesian Tree method
    root = None
    stack = [None]
    for i in xrange(N):
        node = [i,None,None] # [index,LeftChild,RightChild]
        while stack[-1] != None and arr[stack[-1][0]] > arr[i]:
            stack.pop()
        if stack[-1] == None:
            node[1] = root
            root = node
        else:
            node[1] = stack[-1][2]
            stack[-1][2] = node
        stack.append(node)
    
    def min_func(i,j):
        node = root
        while True:
            min_index = node[0]
            if i <= min_index <= j:
                return min_index
            elif min_index < i:
                node = node[2]
            else:
                node = node[1]
    return min_func
