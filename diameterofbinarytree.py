class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]

        def depth(root):
            if not root:
                return 0
            l, r = depth(root.left), depth(root.right)
            ans[0] = max(l+r, ans[0])
            return 1+max(l, r)
        depth(root)
        return ans[0]
