class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlphaNum(ch):
            return (ord('A')<=ord(ch)<=ord('Z') or ord('a')<=ord(ch)<=ord('z')
                or ord('0')<=ord(ch)<=ord('9'))
        left=0
        right=len(s)-1
        while left<right:
            while left<right and  not isAlphaNum(s[left]):
                left=left+1
            while right>left and not isAlphaNum(s[right]):
                right=right-1
            if s[left].lower()!=s[right].lower():
                return False
            left=left+1
            right=right-1
        return True
        