class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def isAna(A):
            dict={}
            for ch in A:
                dict[ch]=dict.get(ch,0)+1
            return dict
        S=isAna(s)
        T=isAna(t)
        if S==T:
            return True
        else:
            return False
        
        