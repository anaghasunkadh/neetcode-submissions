class Solution:
    def isPalindrome(self, s: str) -> bool:
        value=[]
        for char in s:
            if char.isalnum():
                value.append(char.lower())
        s="".join(value)
        def pal(i):
            if i>=len(s)//2:
                return True 
            elif s[i]==s[len(s)-i-1]:
                return pal(i+1)
            else:
                return False
        return pal(0)
        
            
            
                
        