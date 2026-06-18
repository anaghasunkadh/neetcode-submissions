class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        count = 0
        def dfs(node):
            for j in range(n):
                if isConnected[node][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                count = count+1
        return count
        