class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visisted_set=set()
        for num in nums:
            if num in visisted_set:
                return True
            else:
                visisted_set.add(num)
        return False
        
        