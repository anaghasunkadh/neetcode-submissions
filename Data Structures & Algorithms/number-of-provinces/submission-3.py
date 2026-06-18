class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visisted_set=set()
        counter=0
        def bfs(val,isConnected,visisted_set):
        
            queue=collections.deque([val])
            visisted_set.add(val)
            while queue:
                element=queue.pop()
                visisted_set.add(element)
                for i in range(0,len(isConnected)):
                    if isConnected[i][element]==1 and i not in visisted_set:
                        queue.append(i)
        for i in range(0,len(isConnected)):
            if i not in  visisted_set:
                bfs(i,isConnected,visisted_set) 
                counter=counter+1
        return counter
                    