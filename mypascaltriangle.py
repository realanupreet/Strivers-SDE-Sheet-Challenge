n = [0, 1, 0]
r = 5
ans = [n[1:-1]]
if r == 1:
    print(ans)
# print(n)
while r-1 > 0:
    # print(n)
    # print(r-1)
    new = []
    prev = n[0]
    for i in n:
        new.append(prev+i)
        prev = i
    new.append(0)
    n = new
    # print(n)
    ans.append(n[1:-1])
    r -= 1
    pass

print(ans)
