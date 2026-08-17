class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=left+1
        maxi=0
        while 0<=left<len(prices) and 0<=right<len(prices):
            if prices[right]-prices[left]<0:
                left=left+1
            else:
                if right<len(prices):
                    maxi=max(maxi,prices[right]-prices[left])
                    right=right+1
        return maxi      