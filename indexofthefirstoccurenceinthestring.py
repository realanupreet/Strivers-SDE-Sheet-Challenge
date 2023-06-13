# haystack = "sadbutsad"
# needle = "sad"
# haystack = "hellow"
# needle = "ll"
haystack = "leetcode"
needle = "leeto"
k = haystack.split(needle)

if needle == "":
    print(0)
i = 0
if len(k) == 1:
    print(-1)
# for a in k:
if k[0] == "":
    print(i)

i += len(k[0])
print(i)
