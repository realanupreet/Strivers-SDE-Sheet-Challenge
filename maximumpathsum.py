# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=[float('-inf')]
        
        def depth(root):
            if not root:
                return 0
            
            l=max(depth(root.left),0)
            
            r=max(depth(root.right),0)
            
            ans[0]=max( ans[0], l+r+root.val )

            return root.val+max(l, r)

        depth(root)
        return ans[0]