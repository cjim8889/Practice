# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: 'TreeNode') -> 'int':
        
        self.maxD = 0
        self.traverse(root, 0)
        return self.maxD

    def traverse(self, node, depth):
        
        if (node == None):
            return

        
        self.maxD = depth if depth > self.maxD else self.maxD

        self.traverse(node.left, depth)
        self.traverse(node.right, depth)
