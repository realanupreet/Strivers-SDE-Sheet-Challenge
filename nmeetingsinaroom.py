start = [10, 11, 20]
end = [20, 25, 30]

new = []
for i, s in enumerate(start):
    new.append([s, end[i], i+1])

new.sort(key=lambda x: x[1])
lastend = 0
ans = []
for n in new:
    # print(n)
    if n[0] > lastend:
        ans.append(n[2])
        lastend = n[1]

# print(ans)
