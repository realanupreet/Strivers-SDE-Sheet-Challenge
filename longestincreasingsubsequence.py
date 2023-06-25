def longestIncreasingSubsequence(arr, n) :
    # Initialization
    dPT = [1 for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                dPT[i] = max(dPT[i], 1 + dPT[j])

    return max(dPT)