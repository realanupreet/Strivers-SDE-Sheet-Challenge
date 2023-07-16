# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root is None:
            return res
        queue = [root]

        while queue:
            l = len(queue)
            cl = []
            # print("queue",queue)
            for _ in range(l):
                ele = queue.pop(0)
                cl.append(ele.val)
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
            res.append(cl)
        # print("res",res)
        return res
