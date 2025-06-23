

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, val):
            if not node:
                return TreeNode(val)
            if val < node.value:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node
        self.root = _insert(self.root, value)

    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.value, end=" ")
                _inorder(node.right)
        _inorder(self.root)
        print()
