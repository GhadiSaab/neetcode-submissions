class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ajd = {}
        for i in range(numCourses):
            ajd[i] = []
        for u,v in prerequisites:
            ajd[u].append(v)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state ==2: return True
            if state ==1: return False

            states[node] = visiting
            for nei in ajd[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True