class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isalnums(A):
            for ch in A:
                return ord("a")<=ord(ch)<=ord("z") or ord("0")<=ord(ch)<=ord("9") or ord("A") <=ord(ch)<=ord("Z")
        left=0
        right=len(s)-1
        while left<right:
            while left<right and not isalnums(s[left]):
                left=left+1
            while right>left and not isalnums(s[right]):
                right=right-1
            if s[left].lower()!=s[right].lower():
                return False
            left=left+1
            right=right-1
        return True

        