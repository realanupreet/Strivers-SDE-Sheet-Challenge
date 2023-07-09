class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in nummap:
                return [nummap[target-num], i]
            nummap[num] = i
