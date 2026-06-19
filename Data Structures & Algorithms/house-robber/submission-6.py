class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def f (i,nums,dp):
            if i==0:
                dp[i]=nums[0]
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick=nums[i]+f(i-2,nums,dp)
            notpick=f(i-1,nums,dp)
            dp[i]=max(pick,notpick)
            return dp[i]
        return f(n-1,nums,dp)
        

        