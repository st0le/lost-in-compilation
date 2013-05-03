import random
N = 10
arr = range(1,N+1)
random.shuffle(arr) #randomize order
r = random.randint(0,N)
arr[r] = 0 # set random element to 0

def missing_number_naive(arr):
    for i in range(1,N+1):
        if i not in arr:
            return i
    return None

def missing_number_linear(arr):
    return (N * (N+1) / 2) - sum(arr)

def missing_number_xor(arr):    
    Q = [N,1,N+1,0][N%4]
    P = 0
    for v in arr:
        P = P ^ v
    return P ^ Q

print arr
print "Naive Method : ",missing_number_naive(arr)
print "Linear Method : ",missing_number_linear(arr)
print "Xor Method : ",missing_number_xor(arr)
