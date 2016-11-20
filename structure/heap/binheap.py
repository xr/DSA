# implement as a minHeap

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percUp(self, i):
		while i // 2 > 0:
			if self.heapList[i]['key'] < self.heapList[i // 2]['key']:
				temp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = temp
			i = i // 2

	def percDown(self, i):
		while (2*i) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i]['key'] > self.heapList[mc]['key']:
				temp = self.heapList[mc]
				self.heapList[mc] = self.heapList[i]
				self.heapList[i] = temp
			i = mc

	def minChild(self, i):
		if 2*i + 1 > self.currentSize:
			return 2*i
		else:
			if self.heapList[i*2]['key'] < self.heapList[i*2 + 1]['key']:
				return i*2
			else:
				return i*2 + 1

	def insert(self, key, data):
		self.heapList.append({
			'key': key,
			'data': data
		})
		self.currentSize += 1
		self.percUp(self.currentSize)

	def delMin(self):
		tbr = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize -= 1
		self.heapList.pop()
		self.percDown(1)
		return tbr


	def __str__(self):
		return ','.join(str(v) for v in self.heapList)

# bh = BinHeap()

# bh.insert(31,'31data')
# bh.insert(2, '2data')
# bh.insert(13, '13data')
# bh.insert(7, '7data')
# bh.insert(23, '23data')
# bh.insert(1, '1data')

# print(bh)
