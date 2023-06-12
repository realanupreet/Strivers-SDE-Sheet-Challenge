# didnt work marked for revisit

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]

# for k in range(3):
#     for j in range(3):
#         print(k, j, " ", sep="", end="")
#     print()

# for g in grid:
# print(g)
bad = 0
badp = []
good = 0
# goodo=[]
goodp = []
for i, g in enumerate(grid):
    for j, a in enumerate(g):
        if a == 1:
            good += 1
            goodp.append(f"{i}-{j}")
            # goodo.append([i,j])
        elif a == 2:
            bad += 1
            badp.append(f"{i}-{j}")
            # bado.append([i,j])
ans = -1


def shit(badp, m):
    global ans
    bado = []
    for b in badp:
        # print(b)
        i = int(b[0])
        j = int(b[-1])
        # print(i,j)
        for k in [[i+1, j], [i, j+1], [i, j-1], [i-1, j]]:
            anushashn = f"{k[0]}-{k[1]}"
            # print(f"{k[0]}-{k[1]}")
            if anushashn in goodp:
                # print("yes")
                goodp.remove(anushashn)
                bado.append(anushashn)
    if not bado:
        # print("-------------------asatya")
        ans = -1
        return
    if goodp:
        return shit(bado, m+1)
    else:
        # print("    ", m+1)
        # global ans
        ans = m+1
        return m+1


print(shit(badp, 0))
print(ans)
