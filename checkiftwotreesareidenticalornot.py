# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        rp,rq = [],[]
        qp, qq=deque(),deque()
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        qp.append(p)
        qq.append(q)
        while qp:
            currentlevel=[]
            size = len(qp)
            for _ in range(size):
                currentnode = qp.popleft()
                currentlevel.append(currentnode.val)
                if currentnode.left:
                    qp.append(currentnode.left)
                else:
                    currentlevel.append("l")
                if currentnode.right:
                    qp.append(currentnode.right)
                else:
                    currentlevel.append("r")
            rp.append(currentlevel)
        while qq:
            currentlevel=[]
            size = len(qq)
            for _ in range(size):
                currentnode = qq.popleft()
                currentlevel.append(currentnode.val)
                if currentnode.left:
                    qq.append(currentnode.left)
                else:
                    currentlevel.append("l")
                if currentnode.right:
                    qq.append(currentnode.right)
                else:
                    currentlevel.append("r")
            rq.append(currentlevel)
        return rq == rp