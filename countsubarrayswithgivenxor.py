from collections import defaultdict

def subarraysWithSumK(a: [int], b: int) -> int:
    xo = 0
    count = 0
    mp = defaultdict(int)
    for i in range(len(a)):
        xo ^= a[i]
        if xo == b:
            count += 1
        if xo ^ b in mp:
            count += mp[xo ^ b]
        mp[xo] += 1
    return count
    pass

