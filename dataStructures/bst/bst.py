class TreeNode:
	def __init__(self,key,val,left=None,right=None,
									   parent=None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild

	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self

	def isRightChild(self):
		return self.parent and self.parent.rightChild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightChild or self.leftChild)

	def hasAnyChildren(self):
		return self.rightChild or self.leftChild

	def hasBothChildren(self):
		return self.rightChild and self.leftChild

	def replaceNodeData(self,key,value,lc,rc):
		self.key = key
		self.payload = value
		self.leftChild = lc
		self.rightChild = rc
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild():
			self.rightChild.parent = self

class BST:
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def get(self, key):
		res = self._get(key, self.root)
		if res:
			return res.payload

	def _get(self, key, currentNode):
		if currentNode:
			print('currentNode.key', currentNode.key)
			print('key', key)
			if key == currentNode.key:
				return currentNode
			elif key < currentNode.key:
				return self._get(key, currentNode.leftChild)
			elif key > currentNode.key:
				return self._get(key, currentNode.rightChild)

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root = TreeNode(key,val)
		self.size = self.size + 1

	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild = TreeNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				if currentNode.key == key:
					currentNode.replaceNodeData(key, val, currentNode.leftChild, currentNode.rightChild)
				else:
					self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild = TreeNode(key,val,parent=currentNode)

	def __len__(self):
		return self.size

	def __setitem__(self,k,v):
		self.put(k,v)

	def __getitem__(self,key):
		return self.get(key)

	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False


a = BST()
a[1] = 'hello'
a[2] = 'world'
print(a.length())
print(len(a))
print(a[2])
print(3 in a)