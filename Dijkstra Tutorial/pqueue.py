#priority queue using min/max heap
import heapq as hp

class pqueue:
	
	def __init__(self, minheap = True):
		self.heap = []
		self.mul = 1 if minheap else -1
		self.count = 0
		
	def size(self):
		return len(self.heap)
	
	def push(self,item):
		if item and isinstance(item, tuple) and isinstance(item[0],int):
			self.count = self.count + 1
			hp.heappush(self.heap,(item[0] * self.mul,self.count) + item[1:])
		else:
			raise Exception("parameter has to be a tuple with the first entry as an integer.")
	
	def pop(self):
		if self.empty(): raise Exception("pqueue is empty.")
		item = hp.heappop(self.heap)
		return (self.mul * item[0],) + item[2:] 
		
	def __str__(self):
		return str(list((self.mul * p, r) for p,q,r in self.heap))

	def __repr__(self):
		return str(list((self.mul * p, r) for p,q,r in self.heap))
		
	def empty(self):
		return len(self.heap) == 0
	
	def clear(self):
		self.heap = []

if __name__ == "__main__":
	import random
	pq = pqueue()
	for i in range(100):
		pq.push((random.randint(-10,10),i))
	print pq

	while not pq.empty():
		print pq.pop()
	raw_input()