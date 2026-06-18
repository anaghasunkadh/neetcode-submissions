class Solution:
    def isPalindrome(self, s: str) -> bool:
        value=[]
        for char in s:
            if char.isalnum():
                value.append(char.lower())
        s="".join(value)
        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return False
            else:
                left=left+1
                right=right-1
        return True
        
        