class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        k = haystack.split(needle)

        if needle == "":
            return(0)
        i=0
        if len(k)==1:
            return(-1)
        # for a in k:
        if k[0]=="":
            return(i)

        i+=len(k[0])
        return(i)