"""
trees.py

Binary Tree Implementation in Python
------------------------------------

A binary tree is a hierarchical data structure where each node has at most two children:
    - Left child
    - Right child

Applications:
-------------
- Hierarchical data representation (file systems, organization charts)
- Searching and sorting (BST)
- Expression parsing
- Pathfinding algorithms
"""

# Node class for binary tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Tree class
class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    # Pre-order traversal: Root -> Left -> Right
    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # In-order traversal: Left -> Root -> Right
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Post-order traversal: Left -> Right -> Root
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    # Level-order traversal (Breadth-first)
    def level_order(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


# -----------------------
# Example Usage
# -----------------------
if __name__ == "__main__":
    # Creating the binary tree
    #          1
    #        /   \
    #       2     3
    #      / \   / 
    #     4   5 6  

    bt = BinaryTree(1)
    bt.root.left = TreeNode(2)
    bt.root.right = TreeNode(3)
    bt.root.left.left = TreeNode(4)
    bt.root.left.right = TreeNode(5)
    bt.root.right.left = TreeNode(6)

    print("Pre-order Traversal:")
    bt.preorder(bt.root)
    print("\nIn-order Traversal:")
    bt.inorder(bt.root)
    print("\nPost-order Traversal:")
    bt.postorder(bt.root)
    print("\nLevel-order Traversal:")
    bt.level_order()
