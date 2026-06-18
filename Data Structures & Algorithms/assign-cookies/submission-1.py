class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cookie=0
        greed=0
        while cookie<len(s) and greed<len(g):
            if g[greed]<=s[cookie]:
                greed=greed+1
            cookie=cookie+1
        return greed
        