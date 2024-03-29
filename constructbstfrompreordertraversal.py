def bstFromPreorder(self, A):
    if not A: return None
    root = TreeNode(A[0])
    i = bisect.bisect(A, A[0])
    root.left = self.bstFromPreorder(A[1:i])
    root.right = self.bstFromPreorder(A[i:])
    return root