class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def isAna(A):
            counts={}
            for char in A:
                counts[char]=counts.get(char,0)+1
            return counts
        StringS=isAna(s)
        stringT=isAna(t)
        if StringS==stringT:
            return True
        return False
        


        