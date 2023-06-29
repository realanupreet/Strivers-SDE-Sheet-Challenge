A = [3, 1, 2, 5, 3]
a = [-1]*len(A)
r = -1
for k in A:
    if a[k-1] == 1:
        r = k
    a[k-1] = 1

m = -1
for i in range(len(A)):
    if a[i] == -1:
        m = i+1

print(m, r)

# nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# k = [-1]*(len(nums)+1)

# for n in nums:
#     k[n] = 0

# for i in range(len(k)):
#     if k[i] == -1:
#         print(i)
