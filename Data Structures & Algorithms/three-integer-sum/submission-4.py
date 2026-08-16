class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for index,value in enumerate(nums):
            if index>0 and nums[index]==nums[index-1]:
                continue
            left=index+1
            right=len(nums)-1
            while left<right:
                if value+nums[left]+nums[right]>0:
                    right=right-1
                elif value+nums[left]+nums[right]<0:
                    left=left+1
                else:
                    res.append([value,nums[left],nums[right]])
                    left=left+1
                    right=right-1
                    while left<right and nums[left]==nums[left-1]:
                        left=left+1
                    while left<right and nums[right]==nums[right+1]:
                        right=right-1
        return res
        