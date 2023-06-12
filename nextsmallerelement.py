class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        # arr=[]
        stack = []
        # ans = []
        for i, a in enumerate(A):
            # print(a)
            ans = -1
            for k in reversed(A[:i]):
                # print("",k)
                if k < a:
                    # print(" Ooh la la")
                    ans = k
                    break
            stack.append(ans)
        return stack
