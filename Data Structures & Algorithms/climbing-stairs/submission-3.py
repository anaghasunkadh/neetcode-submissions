class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        def f(i,dp):
            if i==0 or i==1:
                return 1
            if dp[i]!=-1:
                return dp[i]
            dp[i]=f(i-1,dp)+f(i-2,dp)
            return dp[i]
        return f(n,dp)
        

        
        