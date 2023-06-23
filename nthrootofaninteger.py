from math import *

 

def NthRoot(n, m):

    ans = round(pow(m, (1.0/n)))

    if(pow(ans, n) == m):

        return ans

    else:

        return -1