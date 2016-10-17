class TreeNode:
	def __init__(self, key, val, left=None, right=None, parent=None):
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

	def findSuccessor(self):
		succ = None
		# if the node has rightChild, then just find the min element in the rightSubTree
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					succ = self.parent
				else:
					self.parent.rightChild = None
					succ = self.parent.findSuccessor()
					self.parent.rightChild = self
		return succ

	def findMin(self):
		minimal = self
		while minimal.hasLeftChild():
			minimal = minimal.leftChild
		return minimal

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif self.hasAnyChildren():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftChild = self.leftChild
				else:
					self.parent.rightChild = self.leftChild
					self.leftChild.parent = self.parent
			else:
				if self.isLeftChild():
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
					self.rightChild.parent = self.parent

	def __iter__(self):
		if self:
			if self.hasLeftChild():
				for elem in self.leftChild:
					yield elem
			yield self.key
			if self.hasRightChild():
				for elem in self.rightChild:
					yield elem

class BST:
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def get(self, key):
		res = self._get(key, self.root)
		if res:
			return res

	def _get(self, key, currentNode):
		if currentNode:
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

	def _removeWithTwoChildren(self, targetNode):
		succ = targetNode.findSuccessor()
		succ.spliceOut()
		targetNode.key = succ.key
		targetNode.payload = succ.payload

	def remove(self, targetNode):
		"""
		case 1, node has no children => remove directly
		case 2, node has one child => move the child reference to it's parent
		"""
		if targetNode.isLeaf():
			if targetNode.isLeftChild():
				targetNode.parent.leftChild = None
			else:
				targetNode.parent.rightChild = None
		else:
			if targetNode.hasLeftChild() and not targetNode.hasRightChild():
				# if node has only one left child
				if targetNode.isLeftChild():
					targetNode.parent.leftChild = targetNode.leftChild
					targetNode.leftChild.parent = targetNode.parent
				elif targetNode.isRightChild():
					targetNode.parent.rightChild = targetNode.rightChild
					targetNode.leftChild.parent = targetNode.parent
				else:
					targetNode.replaceNodeData(targetNode.leftChild.key, targetNode.leftChild.payload, targetNode.leftChild.leftChild, targetNode.leftChild.rightChild)

			if targetNode.hasRightChild() and not targetNode.hasLeftChild():
				# if node has only one right child
				# if current node is left child
				if targetNode.isLeftChild():
					targetNode.parent.leftChild = targetNode.leftChild
					targetNode.rightChild.parent = targetNode.parent
				elif targetNode.isRightChild():
					targetNode.parent.rightChild = targetNode.rightChild
					targetNode.rightChild.parent = targetNode.parent
				else:
					targetNode.replaceNodeData(targetNode.rightChild.key, targetNode.rightChild.payload, targetNode.rightChild.leftChild, targetNode.rightChild.rightChild)

			if targetNode.hasRightChild() and targetNode.hasLeftChild():
				self._removeWithTwoChildren(targetNode)


	def delete(self, key):
		if self.size > 1:
			nodeToRemoved = self._get(key, self.root)
			if nodeToRemoved:
				self.remove(nodeToRemoved)
				self.size -= 1
			else:
				raise KeyError('Error, key not in tree')
		elif self.size == 1:
			if key == self.root.key:
				self.root = None
				self.size -= 1
		else:
			raise KeyError('Error, key not in tree')


	def __len__(self):
		return self.size

	def __setitem__(self, k, v):
		self.put(k,v)

	def __getitem__(self, key):
		return self.get(key)

	def __delitem__(self, key):
		self.delete(key)

	def __iter__(self):
		return self.root.__iter__()

	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False


a = BST()
a[17] = '17'
a[5] = '5'
a[35] = '35'
a[2] = '2'
a[11] = '11'
a[29] = '29'

a[38] = '38'
a[9] = '9'
a[16] = '16'

a[7] = '7'
a[8] = '8'
for x in a:
	print(x)
print(a[9].leftChild.payload)
print(a[7].parent.payload)
print(a[17].leftChild.payload)
a.delete(5)
print(a[9].leftChild.payload)
print(a[7].parent.payload)
print(a[17].leftChild.payload)