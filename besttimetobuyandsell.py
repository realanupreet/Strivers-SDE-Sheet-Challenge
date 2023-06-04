def maximumProfit(arr):
    mini = arr[0]
    Max = 0
    for i in range(1, len(arr)):
        cost = arr[i]-mini
        Max = max(Max, cost)
        mini = min(mini, arr[i])

    return Max
