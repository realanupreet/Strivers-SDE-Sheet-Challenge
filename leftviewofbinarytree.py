def LeftView(root):
    ivals = []
    res = []

    def genleft(root, i):
        if not root:
            return
        #   global i
        # print(root.data,i)
        if i not in ivals:
            res.append(root.data)
            ivals.append(i)

        k = i+1
        genleft(root.left, k)
        genleft(root.right, k)
        # i+=1
        return [1]

    genleft(root, 0)
    return res
