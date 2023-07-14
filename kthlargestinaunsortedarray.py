import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
# k = 4
        nums=[(-n) for n in nums]
        heapq.heapify(nums)
        while k-1:
            heapq.heappop(nums)
            k -= 1
        # print(-nums[0])
        return -nums[0]
                