root = []
res = []


def preorder(root):
    if not root:
        return
    res.append(root.val)
    preorder(root.left)
    preorder(root.right)


preorder(root)
