nums = [1, 1, 2, 3, 3, 4, 4, 7, 7, 8, 8]
print(nums)
even = []
odd = []
for i in range(len(nums)):
    if i % 2 == 0:
        even.append(nums[i])
    else:
        odd.append(nums[i])

even = set(even)
odd = set(odd)
print(list(even.difference(odd))[0])

# l, r = 0, len(nums)-1
# # print(nums[l],nums[r])
# while l < r:
#     m = (l+r)//2
#     print(m)
#     if nums[m] == nums[m-1]:
#         print(nums[m], nums[m-1])
#         nums.remove(nums[m])
#         nums.remove(nums[m-1])
#         # nums.remove(nums[m-1])
#         r = m - 1
#     elif nums[m] == nums[m+1]:
#         print(nums[m], nums[m+1])
#         nums.remove(nums[m])
#         nums.remove(nums[m+1])
#         l = m
#     else:
#         print("bombastic", nums[m])
#         break

# print("ans", nums[0])
