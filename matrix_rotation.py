import pprint,random

def random_array(sz,low=10,high=100):
    return map(lambda _:random.randint(low,high),xrange(sz))

def random_matrix(m,n):
    return map(lambda _:random_array(n), xrange(m))
m,n = random.randint(4,6),random.randint(4,6)
mtx = random_matrix(m,n)


def transpose(X):
    return map(list,zip(*X))

def reverse_rows(X):
    return map(lambda x:list(reversed(x)),X)

def reverse_cols(X):
    return list(reversed(X))

def rotate_right_90(X):
    return reverse_rows(transpose(X))

def rotate_right_180(X):
    return reverse_rows(reverse_cols(X))

def rotate_left_90(X):
    return reverse_cols(transpose(X))

print "Original Matrix"
pprint.pprint(mtx)
print "90/-270 degree rotation"
pprint.pprint(rotate_right_90(mtx))
print "180/-180 degree rotation"
pprint.pprint(rotate_right_180(mtx))
print "270/-90 degree rotation"
pprint.pprint(rotate_left_90(mtx))
