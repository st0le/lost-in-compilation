import sys
import pprint
mtx = [
     [2,  5,  8, 12 ],
     [4,  7,  9, 17 ],
     [6, 15, 20, 22 ],
     [11, 18, 25, 30],
]

def p(mtx):
    print '\n'.join(map(str,mtx))


def youngify(mtx,i,j):
    if i >= len(mtx) or j >= len(mtx[0]):
        return sys.maxint
    hold = mtx[i][j]
    mtx[i][j] = sys.maxint
    min_i,min_j = i,j
    if i + 1 < len(mtx) and mtx[i+1][j] < mtx[min_i][min_j]:
        min_i,min_j = i+1,j
    if j + 1 < len(mtx[0]) and mtx[i][j+1] < mtx[min_i][min_j]:
        min_i,min_j = i,j+1
    if i != min_i or min_j != j:
        mtx[i][j] = youngify(mtx,min_i,min_j)
    return hold

p(mtx)
while mtx[0][0] != sys.maxint:
    print youngify(mtx,0,0)
p(mtx)