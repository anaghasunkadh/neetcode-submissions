class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visisted_set = set()
        left=0
        right=0
        maxlen=0
        for right in range(len(s)):
            while s[right] in visisted_set:
                visisted_set.remove(s[left])
                left=left+1
            if s[right] not in visisted_set:
                visisted_set.add(s[right])
            
            maxlen=max(maxlen,right-left+1)
        return maxlen





        