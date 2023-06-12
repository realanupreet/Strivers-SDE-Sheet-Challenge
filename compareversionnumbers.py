version1 = "7.5.2.4"
version2 = "7.5.3"
v1 = [int(k) for k in version1.split(".")]
v2 = [int(k) for k in version2.split(".")]

if len(v1) > len(v2):
    v2.extend([0]*(len(v1)-len(v2)))
else:
    v1.extend([0]*(len(v2)-len(v1)))

# v1=int("".join([str(k) for k in v1]))
# v2=int("".join([str(k) for k in v2]))
# if v1<v2:
#     print(-1)
# elif v1>v2:
#     print(1)
# else:
#     print(0)
