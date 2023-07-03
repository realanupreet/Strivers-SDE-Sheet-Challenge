# a better in place O(1) solution
a = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
for m in a:
    print(m)

v = -1
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] == 0:
            a[0][j] = 0
            if i == 0   :
                v = 0
            else:
                a[i][0] = 0

print()
for r in range(1,len(a)):
    for c in range(1,len(a[0])):
        if a[r][0] == 0 or a[0][c] == 0:
            a[r][c] = 0
        # if :
        #     a[r][c] = 0

for m in range(len(a)):
    if a[0][0]==0:
        a[m][0]=0

for m in range(len(a[0])):
    if v == 0:
        a[0][m] = 0


for m in a:
    print(m)
