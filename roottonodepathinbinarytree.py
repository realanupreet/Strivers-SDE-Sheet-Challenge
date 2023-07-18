def allRootToLeaf(root):

    a = []

    def f(root, t):

        if not root:

            return

        if not root.left and not root.right:

            t.append(str(root.data))

            a.append(' '.join(t[:]))

            return

 

        t.append(str(root.data))

        if root.left:

            f(root.left, t)

            t.pop()

        if root.right:

            f(root.right, t)

            t.pop()

 

    f(root, [])

    return a