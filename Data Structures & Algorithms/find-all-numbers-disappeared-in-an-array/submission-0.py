class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        visisted_set = set()
        non_existing = []
        for i in range(len(nums)):
            visisted_set.add(nums[i])
        for i in range(1,len(nums)+1):
            if i not in visisted_set:
                non_existing.append(i)
        return non_existing
            
        