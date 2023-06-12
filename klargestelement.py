# should be acbt aka almost complete binary tree
# import heapq
# heapq.heapify(data)
# heapq.heappush(d)
# heapq.heappop(d)
import heapq
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
nums=[(-n) for n in nums]
heapq.heapify(nums)
while k-1:
    print(heapq.heappop(nums))
    k -= 1
print(-nums[0])
