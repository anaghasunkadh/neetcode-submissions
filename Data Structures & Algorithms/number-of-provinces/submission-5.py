class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        counter=0
        visisted_set=set()
        def bfs(start,isConnected,visisted_set):
            queue=collections.deque()
            queue.append(start)
            while queue:
                element=queue.popleft()
                visisted_set.add(element)
                for (index,value) in enumerate(isConnected[element]):
                    if value==1 and index not in visisted_set:
                        queue.append(index)
        for i in range(len(isConnected)):
            if i not in visisted_set: 
                bfs(i,isConnected,visisted_set)
                counter=counter+1
        return counter
                
        

        