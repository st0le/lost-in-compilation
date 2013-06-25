import random

def random_array(sz,low=10,high=100):
    return map(lambda _:random.randint(low,high), xrange(sz))

R = random_array(random.randint(25,40))

def longest_increasing_subsequence_dfs(lst):
    lis_seq = []
    sz = len(lst)
    def lis(index,seq):
        if len(seq) + (sz - index) < len(lis_seq): return #prune the rest.
        for i in xrange(index,sz):
            if seq[-1] < lst[i]:
                seq.append(lst[i])
                lis(i+1,seq)
                seq.pop()
        else:
            if len(seq) > len(lis_seq):
                l = lis_seq
                l[:] = seq
    for i in xrange(sz):
        lis(i + 1,[lst[i]])
    return lis_seq

def longest_increasing_subsequence_dp(lst):
    if not lst: return None
    lis_len = []
    prev = []
    for i,v in enumerate(lst):
        mx = 0
        mxi = -1
        for j in xrange(i):
            if v > lst[j] and mx < lis_len[j]:
                mx = lis_len[j]
                mxi = j
        lis_len.append(1 + mx)
        prev.append(mxi)
    index = max(xrange(len(lst)),key=lis_len.__getitem__)
    lis = []
    while index >= 0:
        lis.append(lst[index])
        index = prev[index] 
    lis.reverse()
    return lis
    


print R
dfs = longest_increasing_subsequence_dfs(R)
print dfs,len(dfs)
dp = longest_increasing_subsequence_dp(R)
print dp,len(dp)