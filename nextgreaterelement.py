class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nmap = {}
        for i, n in enumerate(nums2):
            nmap[n] = i
        # print(nmap)
        anss = []
        for n in nums1:
            ans = -1
            f = -1
            for i in range(nmap[n]+1, len(nums2)):
                if nums2[i] > n:
                    ans = nums2[i]
                    anss.append(ans)
                    f = 1
                    break
            if f == -1:
                anss.append(ans)

        return anss
