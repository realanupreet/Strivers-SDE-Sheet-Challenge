# inorder is left mid and right
root = []

res = []


def inorder(root):
    if not root:
        return
    inorder(root.left)
    res.append(root.val)
    inorder(root.right)


inorder(root)
