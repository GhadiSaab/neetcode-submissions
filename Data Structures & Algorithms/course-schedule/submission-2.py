class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ajd = {}
        
        for i in range(numCourses):
            ajd[i] = []
        for u,v in prerequisites:
            ajd[u].append(v)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]

            if state is VISITING: return False
            if state is VISITED: return True


            states[node] = VISITING

            for nei in ajd[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            return True


        for node in ajd:
            if not dfs(node):
                return False

        return True  