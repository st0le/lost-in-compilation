import random,bisect

R = list(set(map(lambda x: random.randint(100,999), xrange(100))))
random.shuffle(R)

def longest_increasing_subsequence(W):
    M = [0]
    I = [-1]
    P = []
    for i,v in enumerate(W):
        j = bisect.bisect(M,v)
        if j == len(M):
            M.append(v)
            I.append(i)
        else:
            M[j] = v
            I[j] = i
        P.append(I[j-1])
        
    lis = []
    index = I[-1]
    while index >= 0:
        lis.append(W[index])
        index = P[index]
    lis.reverse()
    return lis

print R
print longest_increasing_subsequence(R)
