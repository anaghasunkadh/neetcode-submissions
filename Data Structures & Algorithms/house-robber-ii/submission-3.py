class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        arr1=nums[0:n-1]
        arr2=nums[1:n]

        def f(nums):
            if len(nums)==0:
                return 0
            if len(nums)==1:
                return nums[0]
            prev2=nums[0]
            prev=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                pick=nums[i]+prev2
                notpick=prev
                current=max(pick,notpick)
                prev2=prev
                prev=current
            return prev
        return max(f(arr1),f(arr2))