from sys import stdin
import sys

# def cutRod(price, n):

#     # Write your code here.
#     pass



def solve(idx,n,arr,dp):
    if idx==0:
        return arr[0]*n
    if dp[idx][n]!=-1:return dp[idx][n]
    skip=0+solve(idx-1,n,arr,dp)
    notskip=float("-inf")
    rodlen=idx+1
    if rodlen<=n:
        notskip=arr[idx]+solve(idx,n-rodlen,arr,dp)
        
    dp[idx][n]=max(notskip,skip)
    return dp[idx][n]
def cutRod(arr, n):
    dp=[[-1]*(n+1) for _ in range(n)]
    return solve(n-1,n,arr,dp)

# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
