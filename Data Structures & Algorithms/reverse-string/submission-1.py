class Solution:
    def reverseString(self, s: List[str]) -> None:
        right=len(s)-1
        left=0
        while left<=right:
            s[left],s[right]=s[right],s[left]
            left=left+1
            right=right-1
        return s

        
        
        