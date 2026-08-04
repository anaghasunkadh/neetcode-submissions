class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count=0
        visisted_set=set()
        queue=collections.deque()
        def bfs(start,visisted_set,queue):
            queue.append(start)
            visisted_set.add(start)
            while queue:
                element=queue.popleft()
                for neighbour in range(len(isConnected)):
                    if neighbour not in visisted_set and isConnected[element][neighbour]!=0:
                        queue.append(neighbour)
                        visisted_set.add(neighbour)
        for i in range(len(isConnected)):
            if i not in visisted_set:
                bfs(i,visisted_set,queue)
                count=count+1
        
        return count
                

        