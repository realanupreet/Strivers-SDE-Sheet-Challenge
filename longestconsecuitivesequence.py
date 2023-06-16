nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

nums = set(nums)
c = -1
for n in nums:
    if n-1 not in nums:
        # new seq
        k = 1
        while n+k in nums:
            k += 1
        # print(k)
        c = max(c, k)
print(c)
