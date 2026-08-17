class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        curr=0
        longest=0
        streak=0
        for num in seen:
            if num-1 not in seen:
                curr=num
                streak=1
            while curr+1 in seen:
                curr=curr+1
                streak+=1
            longest=max(longest,streak)
        return longest
            
                