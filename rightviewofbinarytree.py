class Solution:
    # Function to return list containing elements of right view of binary tree.
    def rightView(self, root):
        ivals = []
        res = []

        def genright(root, i):
            if not root:
                return
            if i not in ivals:
                res.append(root.data)
                ivals.append(i)
            k = i+1
            genright(root.right, k)
            genright(root.left, k)
            # i+=1
            return [1]

        genright(root, 0)
        return res
        # code here
# idk how i got this recursive function, but its working right, so thats fun to go with, worked on leetcode aswell, woohoo
