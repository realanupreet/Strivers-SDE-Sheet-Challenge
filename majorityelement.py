nums = [2, 2, 1, 1, 1, 2, 2]
maxn, maxc = nums[0], 1
for n in nums[1:]:
    if n == maxn:
        maxc += 1
    else:
        maxc -= 1
        if maxc == -1:
            maxn = n
            maxc = 1

print(maxn)
