class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        leni=0
        seen=set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[r])
            leni=max(leni,len(seen))
        return leni

        