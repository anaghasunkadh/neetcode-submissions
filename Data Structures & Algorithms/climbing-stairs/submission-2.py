class Solution:
    def climbStairs(self, n: int) -> int:
        mem=[-1]*(n+1)
        if n==1 or n==2:
            return n
        prev=2
        prev2=1
        for i in range(3,n+1):
            value=prev+prev2
            prev2=prev
            prev=value
        return value
        