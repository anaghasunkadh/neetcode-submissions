class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low=0
        high=1
        while high<len(nums):
            if nums[low]==nums[high]:
                high=high+1
            elif nums[low]!=nums[high]:
                nums[low+1]=nums[high]
                low=low+1
        return low+1
        