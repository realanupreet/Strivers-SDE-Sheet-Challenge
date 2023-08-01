def LongestSubsetWithZeroSum(arr):

    # Write your Code here.
    # Return an integer denoting the answer.
    m ={}
    l = 0
    s = 0
    for i in range(0,len(arr)):
        s+=arr[i]
        if s==0 and l<i+1:
            l = i+1
        if s in m:
            if (i-m[s])>l:
                l = i-m[s]
            continue
        m[s] = i
    return l