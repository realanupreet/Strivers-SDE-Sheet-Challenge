candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8

candidates.sort()
for c in candidates:
    print(c)

res = []
cur = []


def solve(k, total):
    if total == target:
        res.append(cur.copy())
        return
    if total > target:
        return
    prev = -1
    for i in range(k, len(candidates)):
        if candidates[i] == prev:
            continue
        cur.append(candidates[i])
        solve(i+1, total+candidates[i])
        cur.pop()
        prev = candidates[i]


solve(0, 0)
