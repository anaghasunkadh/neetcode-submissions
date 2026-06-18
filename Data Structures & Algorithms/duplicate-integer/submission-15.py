class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visisted_set = set()
        for i in range(len(nums)):
            if nums[i] not in visisted_set:
                visisted_set.add(nums[i])
            else:
                return True
        return False

        