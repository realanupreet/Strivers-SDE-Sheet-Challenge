# dutch national flag algorithm

nums = [2, 0, 2, 1, 1, 0]
nums = nums
low = 0
mid = 0
high = len(nums)-1

while mid <= high:  
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
    elif nums[mid] == 1:
        mid += 1
    elif nums[mid] == 2:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1
