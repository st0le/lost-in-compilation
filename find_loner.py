import random

def random_array(sz,lo=10,hi=100):
    return map(lambda _:random.randint(lo,hi),xrange(sz))

arr = set(random_array(5))
key = arr.pop()
arr = list(arr) + list(arr) + list(arr) + [key]
random.shuffle(arr)

def find_loner2(arr):
    ones = twos = 0
    for v in arr:

def find_loner(arr):
    mx = max(arr)
    pow3 = 1
    loner = 0
    while mx / pow3 > 0:
        s = 0
        for v in arr:
            trigit = (v / pow3) % 3
            s += trigit
        loner += pow3*(s % 3)
        pow3 *= 3
    print loner

print arr
find_loner(arr)