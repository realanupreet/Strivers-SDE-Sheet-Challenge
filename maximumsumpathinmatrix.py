def minSumPath(grid):
    def memoization(i,j,dp,n,m):
        if  i<0 or i>=n or j<0 or j>=m:
            return float('inf')

        if i == n-1 and j == m-1:
            return grid[n-1][m-1]
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        right = grid[i][j] + memoization(i,j+1,dp,n,m)
        down = grid[i][j] + memoization(i+1,j,dp,n,m)

        dp[i][j] = min(right,down)
        return dp[i][j]
    
    def tabulation(n,m):
        dp = [ [0]*m for _ in range(n) ]

        dp[n-1][m-1] = grid[n-1][m-1]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                down = right = float('inf')
                if i==n-1 and j==m-1:
                    continue
                elif i==n-1:
                    right = grid[i][j] + dp[i][j+1] 
                elif j==m-1:
                    down = grid[i][j] + dp[i+1][j]
                else:                        
                    right = grid[i][j] + dp[i][j+1] 
                    down = grid[i][j] + dp[i+1][j]  

                dp[i][j] = min(right,down)
        
        return dp[0][0]
    
    n,m = len(grid),len(grid[0])
    dp = [ [-1]*m for _ in range(n) ]
    # return memoization(0,0,dp,n,m)

    return tabulation(n,m)