nums = [3, 2, 3]
num1 = None
num2 = None
c1 = 0
c2 = 0

for n in nums:
    if n == num1:
        c1 += 1
    elif n == num2:
        c2 += 1
    elif c1 == 0:
        num1 = n
        c1 += 1
    elif c2 == 0:
        num2 = n
        c2 += 1
    else:
        c1 -= 1
        c2 -= 1

c1, c2 = 0, 0
for n in nums:
    if n == num1:
        c1 += 1
    if n == num2:
        c2 += 1

ans = []

if c1 > len(nums)/3:
    ans.append(num1)
if c2 > len(nums)/3:
    ans.append(num2)

print(ans)
