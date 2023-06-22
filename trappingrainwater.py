def getTrappedWater(arr, n):
    if n <= 0:
        return 0

    l, r = 0, n - 1
    leftmax, rightmax = 0, 0
    tot = 0

    while l <= r:
        if arr[l] <= arr[r]:
            if arr[l] > leftmax:
                leftmax = arr[l]
            else:
                tot = tot + (leftmax - arr[l])
            l = l + 1

        else:
            if arr[r] > rightmax:
                rightmax = arr[r]
            else:
                tot = tot + (rightmax - arr[r])
            r = r - 1

    return tot

# Test the function
arr = [3, 0, 0, 2, 0, 4]
n = len(arr)
result = getTrappedWater(arr, n)
print("Trapped Water:", result)
