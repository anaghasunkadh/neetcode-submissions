class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited_set = set()
        counter = 0
        def bfs(start,visited_set,isConnected):
            queue = collections.deque()
            queue.append(start)
            while queue:
                    current = queue.popleft()
                    visited_set.add(current)
                    for j in range(len(isConnected[current])):
                        if j not in visited_set and isConnected[current][j]==1:
                            queue.append(j)
                            visited_set.add(j)
        for i in range(len(isConnected)):
            if i not in visited_set:
                bfs(i,visited_set,isConnected)
                counter = counter+1
        return counter

        