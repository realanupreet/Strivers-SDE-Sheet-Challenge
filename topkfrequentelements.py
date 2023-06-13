nums = [-1,-1]
k = 1

nmap={}

for n in nums:
    if n in nmap:
        nmap[n]+=1
    else:
        nmap[n]=1
arr=[""]*len(nums)
for g in nmap:
    # print(g,nmap[g])
    arr[nmap[g]-1]=arr[nmap[g]-1]+"#"+f"{g}"

ans=[]
for a in arr[::-1]:
    # print(a)
    if a:
        s=[int(ka) for ka in a.split("#")[1:]]
        ans.extend(s)
        if len(ans)==k:
            print(ans)
            break
        if len(ans)>k:
            print(ans[:k])
            break