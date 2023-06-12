# most non optimal, needs to be optimised

A = [83, 30, 42, 34, 16, 40, 59, 5, 31, 78, 7, 74, 87, 22, 46, 25, 73, 71, 30]
B = [83, 30, 42, 34, 16, 40, 59, 5, 31, 78, 7, 74, 87, 22, 46, 25, 73, 71, 30]
C = 11
A.sort(reverse=True)
B.sort(reverse=True)
print(A)
print(B)
# C=1
# if C != 2:
#     A = A[:(C//2-1)]
#     B = B[:(C//2-1)]
print(A)
print(B)
ans = []
for a in A:
    for b in B:
        ans.append(a+b)
ans.sort(reverse=True)
print((ans[:C]))
# for i in range(10):
#     print(A[i]+B[i])

# import heapq
# # A = [1, 4, 2, 3]
# A=[(-ele) for ele in A]
# # B = [2, 5, 1, 6]
# B=[(-ele) for ele in B]
# C = 10
# heapq.heapify(A)
# heapq.heapify(B)
# ans=[]
# i=0
# a=0
# b=0
# while C > 0:
#     # ans.append(heapq.heappop(A) + heapq.heappop(B))
#     if i==0:
#         print("-----------",i)
#         ans.append(A[0]+B[0])
#         print(-A[0],"+",-B[0],-A[0]+-B[0])
#         a=B[0]
#         b=A[0]
#         heapq.heappop(A)
#         heapq.heappop(B)
#         print(-a,"+",-A[0],-A[0]+-a)
#         print(-b,"+",-B[0],-B[0]+-b)
#         a+=A[0]
#         b+=B[0]
#         i=1
#     elif i==1:
#         ans.append(max(a,b))
#         i=2
#     elif i==2:
#         ans.append(min(a,b))
#         a=0
#         b=0
#         i=0

#     # print(C)
#     C -= 1

# ans=[(-ele) for ele in ans]
