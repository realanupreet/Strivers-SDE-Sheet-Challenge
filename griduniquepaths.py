from os import *
from sys import *
from collections import *
from math import *

def uniquePaths(m, n):
	# Write your code here.
	dp=[1 for i in range(n)]
	for i in range(1,m):
		left=1
		for j in range(1,n):
			curr=dp[j]+left
			left=curr
			dp[j]=curr
	return dp[-1]
	pass