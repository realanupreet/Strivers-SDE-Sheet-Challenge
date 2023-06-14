
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
arr.sort()
dep.sort()

p = 1
i = 1
j = 0
mp = 0
while i < len(arr) and j < len(dep):
    if arr[i] < dep[j] or arr[i] == dep[j]:
        i += 1
        p += 1
    else:
        j += 1
        p -= 1
    mp = max(mp, p)
    # i+=1
    # j+=1
print(mp)
