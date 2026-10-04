class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        for u,v in prerequisites:
            adj[u].append(v)

        unvisited,visiting,visited = 2,1,0
        states = [unvisited] * numCourses
 

        def dfs(node):
            state = states[node]
            if state == visiting:
                return False
            if state == visited:
                return True

            states[node] = visiting

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            return True



        for nodes in adj:
            if not dfs(nodes):
                return False

        return True


            

        