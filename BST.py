class Node(object):
	def __init__(self, data):
		self.left = None
		self.val = data
		self.right = None


class BinarySearchTree(object):
	def __init__(self, root):
		self.root = Node(root)


def preorder(self, root):
	if root:
		print(root.val, end=' ')
		preorder(root.left)
		preorder(root.right)
 
bst = BinarySearchTree(3)
bst.root.right = Node(2)
bst.root.left = Node(4)

print(preorder())
