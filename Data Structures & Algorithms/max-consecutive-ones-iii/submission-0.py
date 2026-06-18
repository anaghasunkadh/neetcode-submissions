class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        right=0
        maxlength=0
        count_zero=0
        for right in range(len(nums)):
            if nums[right]==0:
                count_zero=count_zero+1
                while count_zero>k:
                    if nums[left]==0:
                        count_zero=count_zero-1
                    left=left+1
            maxlength=max(maxlength,right-left+1)
        return maxlength





        