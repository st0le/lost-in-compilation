import random
a,b,c = [random.randint(-100,100) for i in range(3)]
print a,b,c
#the actual solution
mx = max(a,max(b,c))
mn = -max(-a,max(-b,-c))
mid = a+b+c-mn-mx
print mn,mid,mx
