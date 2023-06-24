nums1 = [13, 5, 9, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
k = 3
# without extra space


def mooveaage(n, i):
    prev = i
    global k
    k += 1
    for i in range(n, len(nums1)):
        # print(i)
        nums1[i], prev = prev, nums1[i]


for n in nums2:
    f = 0
    for i in range(k):
        if n < nums1[i]:
            f = -1
            print("Kabaaam", n, i)
            mooveaage(i, n)
            break
    # print(n,f,k+1)
    if f == 0:
        nums1[k] = n
        k += 1
        # mooveaage(2, 23)
