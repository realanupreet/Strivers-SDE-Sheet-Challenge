class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = max(nums)
        if max_sum < 0:
            return max_sum
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            current_sum += num
            if current_sum < 0:
                current_sum = 0
            elif max_sum < current_sum:
                max_sum = current_sum

        return max_sum
