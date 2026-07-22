class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visisted_set=set()
        counter=0
        def bfs(start,visisted_set,isConnected):
            queue=collections.deque()
            queue.append((start))
            while queue:
                element=queue.popleft()
                visisted_set.add(element)
                for neighbour in range(len(isConnected)):
                    if neighbour not in visisted_set and isConnected[element][neighbour]==1:
                        queue.append(neighbour)
        for i in range(len(isConnected)):
            if i not in visisted_set:
                bfs(i,visisted_set,isConnected)
                counter=counter+1
        return counter
        