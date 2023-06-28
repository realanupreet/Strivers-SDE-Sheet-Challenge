n = 1
res = []


def pair(n):
    global res
    if n == 1:
        # res="()"
        res.append("()")
        return

    pair(n-1)
    newres = []
    for r in res:
        newres.append("("+r+")")
    newres.append("()"*n)
    res = newres


pair(3)
# res.append("()"*n) if n != 1 else res
