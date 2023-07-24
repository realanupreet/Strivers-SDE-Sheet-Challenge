'''
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''


# This function finds predecessor and successor of key in BST.
# It sets pre and suc as predecessor and successor respectively
class Solution:

    def findPreSuc(self, root, pre, suc, key):
        def copy_node(a, b):
            if b is None:
                return None
            a.key = b.key
            a.left = b.left
            a.right = b.right
        
        def successor(node):
            n1 = None
            while node:
                if node.key<=key:
                    node = node.right
                else:
                    n1 = node
                    node = node.left
            return n1

        
        def predecessor(node):
            n2 = None
            while node:
                if node.key>=key:
                    node = node.left
                else:
                    n2 = node
                    node = node.right
            return n2
        
        n = root
        copy_node(pre,predecessor(root))
        copy_node(suc,successor(n))

        # Your code goes here
