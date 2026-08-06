class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def isAna(A):
            dict={}
            for char in A:
                if char not in dict:
                    dict[char]=0
                else:
                    dict[char]+=1
            return dict
        S=isAna(s)
        T=isAna(t)
        if S==T:
            return True
        else:
            return False
        
         
        
        