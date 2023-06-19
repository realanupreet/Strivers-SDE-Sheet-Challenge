# contains an attempt something quirky which didnt worked out eventually
# l = [3, 4, 5, 6, 7, 8, 6]
# # class Solution:
# # print(len(l))


# def lget(i):
#     if i < len(l)//2:
#         print("   ", (i % (len(l)//2)) - len(l)//2)
#         return((i % (len(l)//2)) - len(l)//2)
#     elif i == len(l)//2:
#         print("   ", 0)
#         return 0
#     else:
#         print("   ", (i)-len(l)//2)
#         return ((i)-len(l)//2)
#     pass


# def actuallget(i):
#     if i == 0:
#         print("   ", len(l)//2)
#     if i < 0 or i > 0:
#         print("   ", len(l)//2+i)
#     # if i>0:
#         # print("   ", len(l))

#     pass


# for i in range(len(l)):
#     print(i, l[ i])
#     # lget(i)
#     actuallget(lget(i))

# res = []

# bmap = {0: 7, 1: 5, 2: 6, -1: 2}
# print(sorted(bmap.keys()))

# def bottom(root, n):
#     if not root:
#         return
#     b[n] = root.val
#     bottom(root.left, n-1)
#     bottom(root.right, n+1)
#     pass
