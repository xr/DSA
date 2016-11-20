class BSTNode:
    """
    Represents nodes in a binary search tree.
    """
    def __init__(self, key, value=None, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def height(self):
        """Return the height of this node."""
        left_height = 1 + self.left.height() if self.left else 0
        right_height = 1 + self.right.height() if self.right else 0
        return max(left_height, right_height)

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def _findMin(self):
        if self.left:
            return self.left._findMin()
        else:
            return self

    def __repr__(self):
        return "<BSTNode: key={!r}, value={!r}>".format(self.key, self.value)


class BSTException(Exception):
    pass


class BST:
    """
    Simple recursive binary search tree implementation.
    """
    def __init__(self, NodeClass=BSTNode):
        self.BSTNode = NodeClass
        self.root = None
        self.nodes = 0
        # Updated after each call to insert
        self.newest_node = None

    def find(self, find_key):
        """Return node with key find_key if it exists. If not, return None. """
        return self._findhelp(self.root, find_key)

    def insert(self, new_key, value=None):
        """Insert a new node with key new_key into this BST,
        increase node count by one and return the inserted node."""
        if self.find(new_key) is not None:
            raise KeyError("This BST already contains key {0!r}".format(new_key))
        self.root = self._inserthelp(self.root, new_key, value, None)
        self.nodes += 1
        return self.newest_node

    def height(self):
        """Return the height of this tree."""
        return self.root.height() if self.root else -1

    def __iter__(self):
        """Return an iterator of the keys of this tree in sorted order."""
        for node in self._visit_inorder(self.root):
            yield node.key

    def __len__(self):
        return self.nodes


    def remove(self, key):
        nodeToBeRemoved = self.find(key)
        if nodeToBeRemoved:
            if self.nodes > 1:
                self._removeHelper(nodeToBeRemoved)
                self.nodes -= 1
                return nodeToBeRemoved
            elif self.nodes == 1:
                if self.root.key == key:
                    self.root = None
                    self.nodes -= 1
                    return nodeToBeRemoved

    def _removeHelper(self, targetNode):
        if not targetNode.right and not targetNode.left:
            if targetNode.isLeftChild():
                targetNode.parent.left = None
            else:
                targetNode.parent.right = None

        elif targetNode.right and targetNode.left:
            self._removeNodeWithTwoChildren(targetNode)

        elif targetNode.right:
            self._removeNodeWithRightChild(targetNode)

        elif targetNode.left:
            self._removeNodeWithLeftChild(targetNode)


    def _removeNodeWithLeftChild(self, targetNode):
        if targetNode.parent:
            if targetNode.isLeftChild():
                targetNode.parent.left = targetNode.left
                targetNode.left.parent = targetNode.parent
                if self.root.left == targetNode:
                    self.root.left = targetNode.left
                    targetNode.left.parent = self.root
            else:
                targetNode.parent.right = targetNode.left
                targetNode.left.parent = targetNode.parent
                if self.root.right == targetNode:
                    self.root.right = targetNode.left
                    targetNode.left.parent = self.root
        else:
            self.root = targetNode.left
            targetNode.left.parent = None

    def _removeNodeWithRightChild(self, targetNode):
        if targetNode.parent:
            if targetNode.isLeftChild():
                targetNode.parent.left = targetNode.right
                targetNode.right.parent = targetNode.parent
                if self.root.left == targetNode:
                    self.root.left = targetNode.right
                    targetNode.right.parent = self.root
            else:
                targetNode.parent.right = targetNode.right
                targetNode.right.parent = targetNode.parent
                if self.root.right == targetNode:
                    self.root.right = targetNode.right
                    targetNode.right.parent = self.root
        else:
            self.root = targetNode.right
            targetNode.right.parent = None

    def _removeNodeWithTwoChildren(self, targetNode):
        succ = targetNode.right._findMin()
        if succ.isLeftChild():
            succ.parent.left = succ.right
            if succ.right:
                succ.right.parent = succ.parent
        else:
            succ.parent.right = succ.right
            if succ.right:
                succ.right.parent = succ.parent

        succ.left = targetNode.left
        if targetNode.left:
            targetNode.left.parent = succ

        succ.right = targetNode.right
        if targetNode.right:
            targetNode.right.parent = succ

        if targetNode.parent:
            if targetNode.isLeftChild():
                targetNode.parent.left = succ
                succ.parent = targetNode.parent
                if self.root.left == targetNode:
                    self.root.left = succ
                    succ.parent = self.root
            else:
                targetNode.parent.right = succ
                succ.parent = targetNode.parent
                if self.root.right == targetNode:
                    self.root.right = succ
                    succ.parent = self.root
        else:
            self.root = succ
            succ.parent = None

    def _findhelp(self, node, find_key):
        """Starting from node, search for node with key find_key and return that node.
        If no node with key find_key exists, return None."""
        if node is None or find_key == node.key:
            # End search
            return node

        if find_key < node.key:
            return self._findhelp(node.left, find_key)
        else:
            return self._findhelp(node.right, find_key)

    def _inserthelp(self, node, new_key, value, parent):
        """Starting from node, find an empty spot for the new node and
        insert it into this BST."""
        if node is None:
            # Found an empty spot, create a new node
            self.newest_node = self.BSTNode(new_key, value, parent)
            return self.newest_node

        # Implement functionality to recursively insert nodes
        if new_key < node.key:
            node.left = self._inserthelp(node.left, new_key, value, node)
        else:
            node.right = self._inserthelp(node.right, new_key, value, node)

        return node

    def _visit_inorder(self, node):
        """Return an iterator of the nodes of this tree in inorder starting at node."""
        if node is None:
            return

        # Implement this method to return an iterator (a list will do also)
        # yielding the nodes of this tree in inorder.
        if node.left:
            for elem in self._visit_inorder(node.left):
                yield elem
        yield node
        if node.right:
            for elem in self._visit_inorder(node.right):
                yield elem
