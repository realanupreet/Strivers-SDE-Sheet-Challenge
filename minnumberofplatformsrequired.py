# basically didnt work though im proud of this solution, it was my sole solution

# # print(int("0900"))
# arr = [50,120,200,550,700,850]
# dep = [500,550,1200,700,1100,1000]
# new = []

# for i in range(len(arr)):
#     new.append([arr[i], dep[i]])

# new.sort(key=lambda x: x[0])
# train = set()
# maxs=0
# for n in new:
#     flag = True
#     print(new)
#     tram = train.copy()
#     for t in tram:
#         # print(t)
#         if n[0] > t:
#             train.discard(t)
#             train.add(n[1])
#             flag = False
#     # print(train)
#     # print(tram)
#     # train = tram.copy()
#     maxs = max(maxs, len(tram))
#     if flag:
#         train.add(n[1])

# print(f"""---------
# {maxs}
# ---------""")
# # print()
