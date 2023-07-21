class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = deque()
        maximum = 0
        queue.append(root)
        while queue:
            maximum += 1
            size = len(queue)
            for _ in range(size):
                currentnode = queue.popleft()
                if currentnode.left:
                    queue.append(currentnode.left)
                if currentnode.right:
                    queue.append(currentnode.right)
        return maximum
