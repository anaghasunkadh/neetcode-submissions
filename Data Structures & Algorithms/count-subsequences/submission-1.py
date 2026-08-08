class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[-1 for _ in range(n)]for _ in range(m)]
        
        def f(i,j,s,t):
            if j<0:
                return 1
            if i<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==t[j]:
                dp[i][j]=f(i-1,j-1,s,t)+f(i-1,j,s,t)
            else:
                dp[i][j]=f(i-1,j,s,t)
            return dp[i][j]
        return f(m-1,n-1,s,t)
        