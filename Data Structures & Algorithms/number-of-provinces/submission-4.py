class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visisted_set=set()
        counter=0
        def bfs(isConnected,start,visisted_set):
            queue=collections.deque()
            queue.append(start)
            while queue:
                element=queue.popleft()
                visisted_set.add(element)
                for i in range(len(isConnected)):
                    if isConnected[i][element]==1 and i not in visisted_set:
                        queue.append(i)
        for i in range(len(isConnected)):
            if i not in visisted_set:
                bfs(isConnected,i,visisted_set)
                counter=counter+1
        return counter


        
        