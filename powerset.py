def pwset(v):
    ipt = v
    opt = []
    sol = []
    mapp = {}

    def solve(ip, op):
        if len(ip) == 0:
            sol.append(op)
            return
        op1 = op
        op2 = [ip[0]] + op
        ip = ip[1:]
        solve(ip, op1)
        solve(ip, op2)
    solve(ipt, opt)
    for s in sol:
        if tuple(sorted(s)) not in mapp:
            mapp[tuple(sorted(s))] = 1
    newsol = []
    for k in mapp.keys():
        newsol.append(list(k))
    return sorted(newsol)
