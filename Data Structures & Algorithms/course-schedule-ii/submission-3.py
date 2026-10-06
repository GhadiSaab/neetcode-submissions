class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { }
        res = []
        for i in range(numCourses):
            adj[i] = []
        for u,v in prerequisites:
            adj[u].append(v)

        visited,visiting, unvisited = 2,1,0
        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]
            if state == visited: 
                return True
            if state ==visiting:
                return False

            states[node] = visiting

            for nei in adj[node]:
                if not dfs(nei):
                    return False

            states[node] = visited
            res.append(node)
            return True

        for nodes in adj:
            if not dfs(nodes):
                return []
        return res
