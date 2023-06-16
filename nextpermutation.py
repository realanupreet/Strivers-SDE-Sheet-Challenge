nums = [1, 3, 2]

# Output: [1,4,2,3,5]
prev = -1
j = -1
for i in range(len(nums)-1, -1, -1):
    # print(i, nums[i])
    if nums[i] < prev:
        # print("found", nums[i], i)
        j = i
        break
    prev = nums[i]
print()
if j == -1:
    # print("IM SCREAMING")
    nums = nums[::-1]+[]
if j != -1:
    k = -1
    for i in range(len(nums)-1, -1, -1):
        # print(i)
        if nums[i] > nums[j]:
            # print("found", i, nums[i])
            k = i
            break
    tmp = nums[j]
    nums[j] = nums[k]
    nums[k] = tmp
    nums = nums[:j+1]+sorted(nums[j+1:])
