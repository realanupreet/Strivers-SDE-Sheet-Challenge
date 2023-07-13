def countWaysToMakeChange(arr, amount) :
    def memoization(i,target,arr,dp):
        # return 1 if target is attainable using arr[0] else 0
        if i==0:
            return target%arr[0]==0

        if dp[i][target]!=-1:
            return dp[i][target]

        not_take = memoization(i-1,target,arr,dp)
        take=0
        if arr[i]<=target:
            take = memoization(i,target-arr[i],arr,dp)

        dp[i][target] = not_take+take
        return dp[i][target]
    
    def tabulation(n,arr):
        dp = [ [0]*(amount+1) for _ in range(n)]

        for target in range(amount):
            dp[0][target] = target%arr[0]==0
        
        for i in range(1,n):
            for target in range(0,amount+1):
                not_take = memoization(i-1,target,arr,dp)
                take=0
                if arr[i]<=target:
                    take = memoization(i,target-arr[i],arr,dp)

                dp[i][target] = not_take + take

        return dp[i][target]
    
    n = len(arr)
    arr = sorted(arr)

    # # For memoization
    # dp = [[-1]*(amount+1) for _ in range(n)]
    # return  memoization(n-1,amount,arr,dp)

    # For tabulation
    return tabulation(n,arr)