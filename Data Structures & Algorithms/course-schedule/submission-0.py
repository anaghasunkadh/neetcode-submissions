class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree=[0]*numCourses
        queue=collections.deque()
        graph = collections.defaultdict(list)
        counter=0
        for i in range(len(prerequisites)):
            course,pre=prerequisites[i]
            in_degree[course]+=1
            graph[pre].append(course)
        for i in range(len(in_degree)):
            if in_degree[i]==0:
                queue.append(i)
        while queue:
            element=queue.popleft()
            counter=counter+1
            for neighbour in graph[element]:
                in_degree[neighbour]-=1
                if in_degree[neighbour]==0:
                    queue.append(neighbour)
        if counter==numCourses:
            return True
        else:
            return False

        
        