class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        def isAna(c):
            dict={}
            for str in c:
                dict[str]=dict.get(str,0)+1
            return dict
        S=isAna(s)
        T=isAna(t)
        if S==T:
            return True
        else:
            return False

        