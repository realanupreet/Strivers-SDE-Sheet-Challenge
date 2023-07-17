# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        ltr = True
        if not root:
            return res
        q = [root]
        while q:
            l = len(q)
            level = []
            for _ in range(l):
                e = q.pop(0)
                if ltr:
                    level.append(e.val)
                else:
                    level.insert(0, e.val)

                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)

            ltr = not ltr
            res.append(level)

        return res
