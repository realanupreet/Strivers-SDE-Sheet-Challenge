class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # def fun(strs):
        res = ""
        for l in range(len(strs[0])):
            for s in strs:
                # print(strs[0][l],s[l])
                if l == len(s) or s[l] != strs[0][l]:
                    return res
            res += strs[0][l]
        return res
