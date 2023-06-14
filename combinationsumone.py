candidates = [2, 3, 6, 7]

target = 7
res = []
cur = []


def solve(i, total):
    if total == target:
        res.append(cur.copy())
        return
    if i >= len(candidates) or total > target:
        return

    cur.append(candidates[i])
    solve(i, total+candidates[i])
    cur.pop()
    solve(i+1, total)
    # nonlocal cur
    pass


solve(0, 0)
