class TreeNode:    # Creating and initializing TreeNode class
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):   # define a mechanism to insert nodes in the tree
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):# an _insert method, which is a helper function and does the actual insertion. This method is recursive, meaning it calls itself to traverse the tree until the appropriate location for the new node is found.
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node
    
    def search(self, key): # Internally, search delegates the actual search logic to the private _search method that performs the actual recursive search within the binary search tree.
        return self._search(self.root, key)
    
    def _search(self, node, key): # a base case for the recursive search.
        if node is None or node.key == key:
            return node
        if key < node.key: # If the second if statement is not True, it means that the target key is greater than or equal to the current node key.
            return self._search(node.left, key)
        return self._search(node.right, key) # In a binary search tree, if the target key is greater than the current node's key, the search continues in the right subtree.
            