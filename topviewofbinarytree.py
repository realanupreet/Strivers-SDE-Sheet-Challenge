def topView(self,root):
        res = []
        if not root:
            return res
        q = deque([(root, 0)])
        mp = {}
        while q:
            node, line = q.popleft()
            if line not in mp.keys():
                mp[line] = node.data
            if node.left:
                q.append((node.left, line - 1))
            if node.right:
                q.append((node.right, line + 1))
        for key in sorted(mp.keys()):
            res.append(mp[key])
        return res