def findCeil(root, x):
    ceil=-1
    while root:
        if root.data==x:
            ceil=root.data
            return ceil
        if x>root.data:
            root=root.right
        else:
            ceil=root.data
            root=root.left
    return ceil