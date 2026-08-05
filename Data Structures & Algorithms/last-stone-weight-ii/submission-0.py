class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum=0
        for i in range(len(stones)):
            sum=sum+stones[i]
        target=sum//2
        n=len(stones)
        dp=[[-1 for _ in range(target+1)]for _ in range(n)]
        def f(ind,target):
            if ind==0:
                if stones[0]<=target:
                    return stones[0]
                else:
                    return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            not_pick=f(ind-1,target)
            pick=float('-inf')
            if stones[ind]<=target:
                pick=stones[ind]+f(ind-1,target-stones[ind])
            dp[ind][target]= max(pick,not_pick)
            return dp[ind][target]
        best=f(n-1,target)
        ans=sum-2*best
        return ans

        