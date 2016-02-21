import operator

class Dict(dict):
	def __init__(self):
		self._dict = {}
	
	def add(self, id, val):
		self._dict[id] = val
		
	def get(self, id):
		return self._dict[id]
		
	def getSize(self):
		return len(self._dict)

	def getMax(self):
		return max(self._dict.iteritems(), key=operator.itemgetter(1))[0]
		
	def getMin(self):
		return min(self._dict.iteritems(), key=lambda x: x[1])
		
	def remove(self, id):
		del self._dict[id]	