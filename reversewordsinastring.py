s="a good   example"
s = s.strip().split(" ")
k = []
while s:
    a=s.pop()
    if a != "":
        k.append(a) 
    # print(a)
print(" ".join(k))

