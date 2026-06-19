class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2=cost[0]
        prev=cost[1]
        for i in range(2,len(cost)):
            current=cost[i]+min(prev2,prev)
            prev2=prev
            prev=current
        return min(prev,prev2)
        