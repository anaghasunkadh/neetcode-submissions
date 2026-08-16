class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def Ana(A):
            dict={}
            for char in A:
                dict[char]=dict.get(char,0)+1
            return dict
        S=Ana(s)
        T=Ana(t)
        if S==T:
            return True
        else:
            return False




        