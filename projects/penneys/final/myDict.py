import operator

class Dict(dict):
	def __init__(self):
		self._dict = {}
	
	def add(self, id, val):
		self._dict[id] = val
		
	def get(self, id):
		if id in self._dict:
			return self._dict[id]
		else:
			return None
		
	def getSize(self):
		return len(self._dict)

	def getMax(self):
		maxKey = max(self._dict.iteritems(), key=operator.itemgetter(1))[0]
		maxValue = self.get(maxKey)
		return (maxKey, maxValue)
		
		
	def getMin(self):
		minKey = min(self._dict.iteritems(), key=lambda x: x[1])
		return minKey
		
	def remove(self, id):
		del self._dict[id]
		
	def clear(self):
		self._dict.clear()
		
	def foreach(self, function, option):
		for k, v in sorted(self._dict.items()):
			function(k, v)
			
	def traversal(self, k, v):
		print k, v
		
	def isEmpty(self):
		return not self._dict