class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        visisted_list=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                visisted_list.append(nums[i])
        for i in range(len(visisted_list)):
            nums[i]=visisted_list[i]
        for i in range(len(visisted_list),len(nums)):
            nums[i]=0
        