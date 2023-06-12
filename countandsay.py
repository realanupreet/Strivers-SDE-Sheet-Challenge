def givestr(a):
    ans = ""
    i = 0
    while i < len(a):
        l = i
        k = a[i]
        while i+1 < len(a) and a[i] == a[i+1]:
            i += 1
        i += 1
        ans += f"{i-l}{k}"
    return ans


def countAndSay(n):
    # print("called", n)
    if n == 1:
        return "1"
    k = countAndSay(n-1)
    # print("k is say", givestr(k), "n is", n)
    return givestr(k)


print(countAndSay(4))
# print("---------")

# print(givestr("34"))
