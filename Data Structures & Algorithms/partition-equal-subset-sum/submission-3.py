class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum=0
        n=len(nums)
        for i in range(len(nums)):
            sum=sum+nums[i]
        if sum%2!=0:
            return False
        else:
            target=sum//2
        dp=[[-1 for _ in range(target+1)] for _ in range(n)]
        def f(ind,target):
            if dp[ind][target]!=-1:
                return dp[ind][target]
            if ind==0:
                if nums[0]==target:
                    return True
                else:
                    return False
                if target==0:
                    return True
            not_pick=f(ind-1,target)
            pick=False
            if nums[ind]<=target:
                pick=f(ind-1,target-nums[ind])
            dp[ind][target]= pick or not_pick
            return dp[ind][target]
        ans=f(n-1,target)
        return ans
            
            
        