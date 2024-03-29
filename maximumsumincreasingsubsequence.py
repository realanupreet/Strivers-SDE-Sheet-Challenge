def maxIncreasingDumbbellsSum(rack, n):
    def memoization(idx,prev_idx,dp):
        if idx == n:
            return 0

        if dp[idx][prev_idx+1] != -1:
            return dp[idx][prev_idx+1]
        
        not_take = 0 + memoization(idx+1,prev_idx,dp) # Dont take current index
        
        take = 0
        if prev_idx == -1 or rack[idx] > rack[prev_idx]:
            take = rack[idx] + memoization(idx+1,idx,dp)  # Take current index
        
        dp[idx][prev_idx+1] = max(not_take, take)
        return dp[idx][prev_idx+1]
    
    def tabulation():
        dp = [ [0]*(n+1) for _ in range(n+1) ]

        for idx in range(n-1,-1,-1):
            for prev_idx in range(idx-1,-2,-1):

                not_take = 0 + dp[idx+1][prev_idx+1] # Dont take current index
                
                take = 0
                if prev_idx == -1 or rack[idx] > rack[prev_idx]:
                    take = rack[idx] + dp[idx+1][idx+1] # Take current index
                
                dp[idx][prev_idx+1] = max(take, not_take)
        
        return dp[0][-1+1]


    
    # For memoization
    dp = [ [-1]*(n+1) for _ in range(n+1) ]
    return memoization(0,-1,dp)

    # # For tabulation
    # return tabulation()