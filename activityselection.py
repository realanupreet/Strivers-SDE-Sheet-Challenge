start = [1, 6, 2, 4]
end = [2, 7, 5, 8]

new = []
for i in range(len(start)):
    new.append([start[i], end[i]])

new.sort(key=lambda x: x[1])
a = 0
prev = 0
for n in new:
    print(n)
    if n[0] >= prev:
        prev = n[1]
        a += 1
