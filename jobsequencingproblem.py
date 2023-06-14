# gave a tle, worked on coding ninjas

jobs = [(2, 50)]

jobs.sort(key=lambda x: x[1], reverse=True)
t = 0
p = 0
# d = [0]*(len(jobs)+2)
d = [0] * (max(jobs, key=lambda x: x[0])[0] + 2)
for j in jobs:
    print(j)
    k = j[0]
    print(k, d[k])
    while k > 0 and d[k] != 0:
        k -= 1
    # if d[k] == 0:
    if k != 0:
        d[k] = 1
        t += 1
        p += j[1]
# print(t, p)
print(p)
