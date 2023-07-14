from os import *
from sys import *
from collections import *
from math import *

def nod(t,time):
    days = 0
    ct = 0
    for i in time:
        if ct+i <= t:
            ct += i
        else:
            days += 1
            ct = i
    
    days += 1
    return days


def ayushGivesNinjatest(n, m, time):
    # Write your code here.
    if n >= m:
        return max(time)
    else:
        
        low = max(time)
        high = sum(time)
        ans = 0

        while low <= high :
            mid = (low+high)//2   # ans to be checked 
            days = nod(mid,time)

            if days > n :
                low = mid+1
            elif days <= n:
                high = mid-1
                ans = mid
                
        return ans

            
