# wrong answer and im tired for this binary search approach

# nums = [1, 1, 2]

# l, r = 0, len(nums)-1

# while l <= r:
#     m = l+(r-l)//2
#     if nums[m] == nums[m-1]:
#         lsize = m-1
#     elif nums[m] == nums[m+1]:
#         lsize = m
#     else:
#         print(nums[m])

#     if lsize % 2:
#         r = m-1
#     else:
#         l = m+1
#     # break
