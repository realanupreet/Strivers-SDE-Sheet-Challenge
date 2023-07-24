class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def isParentSum(root):
    if root is None:
        return True
    if not root.left and not root.right:
        return True
    if root.left and root.right and root.left.data + root.right.data != root.data:
        return False
    if root.left and not root.right and root.left.data != root.data:
        return False
    if root.right and not root.left and root.right.data != root.data:
        return False
    return isParentSum(root.left) and isParentSum(root.right)
