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
			if targetNode.hasLeftChild():
				# if node has only one left child
				if not targetNode.hasRightChild():
					# if current node is left child
					if targetNode.isLeftChild():
						targetNode.parent.leftChild = targetNode.leftChild
						targetNode.leftChild.parent = targetNode.parent
					elif targetNode.isRightChild():
						targetNode.parent.rightChild = targetNode.rightChild
						targetNode.leftChild.parent = targetNode.parent
					else:
						targetNode.replaceNodeData(targetNode.leftChild.key, targetNode.leftChild.payload, targetNode.leftChild.leftChild, targetNode.leftChild.rightChild)
				else:
					# node has both left and right
					pass

			if targetNode.hasRightChild():
				# if node has only one right child
				if not targetNode.hasLeftChild():
					# if current node is left child
					if targetNode.isLeftChild():
						targetNode.parent.leftChild = targetNode.leftChild
						targetNode.rightChild.parent = targetNode.parent
					elif targetNode.isRightChild():
						targetNode.parent.rightChild = targetNode.rightChild
						targetNode.rightChild.parent = targetNode.parent
					else:
						targetNode.replaceNodeData(targetNode.rightChild.key, targetNode.rightChild.payload, targetNode.rightChild.leftChild, targetNode.rightChild.rightChild)
				else:
					# node has both left and right
					pass


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
a[17] = '17'
a[5] = '5'
a[25] = '25'
a[2] = '2'
a[11] = '11'
a[35] = '35'

a[9] = '9'

a[16] = '16'

a[29] = '29'
a[38] = '38'
a[7] = '7'

print(a[17].rightChild.payload)
print(a[35].parent.payload)
print('remove...')
a.delete(25)
print(a[17].rightChild.payload)
print(a[35].parent.payload)