class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def isPalindrome(start,end,s):
            while start<=end:
                if s[start]==s[end]:
                    start=start+1
                    end=end-1
                else:
                    return False
            return True
        while l<=r:
            if s[l]==s[r]:
                l=l+1
                r=r-1
            elif s[l]!=s[r]:
                return isPalindrome(l+1,r,s) or isPalindrome(l,r-1,s)
        return True