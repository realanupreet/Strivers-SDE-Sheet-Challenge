def kthLargest(self,root, k):
        #your code here
        res = []
        def bfs(root):
            if not root:
                return
            bfs(root.left)
            res.append(root.data)
            bfs(root.right)
        bfs(root)
        return res[len(res) - k]