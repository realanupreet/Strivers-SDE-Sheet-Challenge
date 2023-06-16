def chkpal(stri):
    return (stri == stri[::-1])

# print(chkpal("aba"))


s = "aab"
res = []
cur = []


def solve(i):
    if i >= len(s):
        res.append(cur.copy())
        return
    for k in range(i, len(s)):
        if chkpal(s[i:k+1]):
            cur.append(s[i:k+1])
            solve(k+1)
            cur.pop()


solve(0)
