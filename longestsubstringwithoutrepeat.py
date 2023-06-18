s = "dvdf"
se = []
m = 0
# f = -1
for k in s:
    if k not in se:
        se.append(k)
        print(k, se)
    else:
        # f = 0
        m = max(m, len(se))
        while k in se:
            se.pop(0)
        se.append(k)
        print(se)
    pass
m = max(m, len(se))
