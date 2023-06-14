n = 3
w = 50
values = [60, 100, 120]
weight = [10, 20, 30]

new = []
for i in range(n):
    new.append([values[i], weight[i], values[i]/weight[i]])

p = 0
new.sort(key=lambda x: x[2], reverse=True)
for n in new:
    print(n)
    if w-n[1] >= 0:
        w = w-n[1]
        p += n[0]
    elif w-n[1] < 0:
        p += n[2]*w
        w = 0
        break
    else:
        break
print(p)


# finaaly done T-T
