"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None: return
        q=[root]
        while q:
            l=len(q)
            pnode=None
            for k in range(l):
                e=q.pop(0)
                if pnode: pnode.next=e
                pnode=e
                if e.left: q.append(e.left)
                if e.right: q.append(e.right)
        return root