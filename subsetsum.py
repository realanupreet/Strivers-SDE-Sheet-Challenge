class Solution:
    def subsetSums(self, arr, N):
        msum = 0
        res = []

        def gen(i):
            nonlocal msum
            if i >= len(arr):
                res.append(msum)
                return
            msum += arr[i]
            gen(i + 1)
            msum -= arr[i]
            gen(i + 1)

        gen(0)
        return res
