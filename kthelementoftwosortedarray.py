"""
    Time complexity: O(log(K))
    Space complexity: O(log(K))
    where K denotes the Kth person in line waiting to be served.
"""

def ninjaAndLadoos(row1, row2, m, n, k):
    # If length of first array is smaller then length of second then swap both the arrays.
    if m > n:
        return ninjaAndLadoos(row2, row1, n, m, k)
    if m == 0:
        return row2[k - 1]
    # If k is equal to 1
    if k == 1:
        return min(row1[0], row2[0])
    i = min(m, k // 2)
    j = min(n, k // 2)
    # If row1[i - 1] is greater than row2[j - 1]
    if row1[i - 1] > row2[j - 1]:
        newRow2 = row2[j:]
        return ninjaAndLadoos(row1, newRow2, m, n - j, k - j)
    newRow1 = row1[i:]
    return ninjaAndLadoos(newRow1, row2, m - i, n, k - i)
    pass

