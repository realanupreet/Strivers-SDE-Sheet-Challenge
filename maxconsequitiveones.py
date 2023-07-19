def longestSubSeg(arr, n, k):
    left = 0
    max_length = 0
    zeros = 0

    for right in range(len(arr)):
        if arr[right] == 0:
            zeros += 1

        while zeros > k:
            if arr[left] == 0:
                zeros -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length