def floorInBST(root, x, floor=-1):

    if root == None:

        return floor

    if root.data==x:

        return root.data

    if root.data<x:

        floor=root.data

        return floorInBST(root.right, x, floor)

    else:

        return floorInBST(root.left, x, floor)