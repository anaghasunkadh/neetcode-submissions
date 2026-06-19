class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        dp[0]=nums[0]
        if n>1:
            dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            if dp[i]!=-1:
                return dp[i]
            pick=nums[i]+dp[i-2]
            notpick=dp[i-1]
            dp[i]=max(pick,notpick)
        return dp[-1]
        
        

        