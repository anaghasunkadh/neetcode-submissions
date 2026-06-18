class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arraySet = set()
        for num in nums:
            if num  in arraySet:
                return True
            else:
                arraySet.add(num)
        return False
                



    
