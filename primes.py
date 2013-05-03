import random

def fermatPass(n):
	return n > 1 and ( n == 2 or ( n % 2 != 0 and pow( random.randint( 1, n - 1 ), n - 1, n ) == 1 ) )

def millerRabin(n, k = 5):
	if n <= 3 or n % 2 == 0: return n == 2 or n == 3
	d = n - 1
	s = 0
	while d > 0 and d % 2 == 0:
		d = d / 2
		s = s + 1

	def millerRabinPass(a, s, d, n):
		x = pow(a, d, n)
		if x == 1: return True
		for i in xrange(s - 1):
			if x == n - 1: return True
			x = (x * x) % n
		return x == n - 1

	return all(millerRabinPass( random.randint( 2, n - 2 ), s, d, n) for _ in xrange(k))
	
def fermatTest(n,k = 10):
	return all( fermatPass( n ) for i in xrange(k) )
	
def lucasLehmerTest(p): #checks if 2^p - 1 is a prime (also called a mersenne prime)
	if p % 2 == 0 and not isPrime(p): return False 
	s = 4
	M = (1 << p) - 1
	for _ in xrange(p - 2):
		s = ((s * s) - 2) % M
	return s == 0
	
def isPrime(n):
	if n <= 3 or n % 2 == 0 or n % 3 == 0: return n == 2 or n == 3 
	for i in xrange(5, int(n**0.5)+1, 6):
		if n % i == 0 or n % (i + 2) == 0:
			return False
	return True

if __name__ == "__main__":
	N = 3000
	fermatPrimes = list(filter(fermatTest,xrange(N)))
	millerPrimes = list(filter(millerRabin,xrange(N)))
	trailDivPrimes = list(filter(isPrime,xrange(N)))
	mersennePrimes = list(filter(lucasLehmerTest,xrange(N)))
	print mersennePrimes
	print set(fermatPrimes) - set(trailDivPrimes) 
	print set(millerPrimes) - set(trailDivPrimes) 
