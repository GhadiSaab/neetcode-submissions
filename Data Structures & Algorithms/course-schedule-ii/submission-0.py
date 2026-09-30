class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ajd = {}
        res =[]
        passed = {}
        for i in range(numCourses):
            ajd[i] = []

        for u,v in prerequisites:
            ajd[u].append(v)

        visited = 2
        visiting = 1
        unvisited = 0

        states = [unvisited] * numCourses
        
        # our function will return an array construsted from the end call to the first
        def dfs(node):
            state = states[node]
            if state == visited: return True
            if state == visiting: return False

            states[node] = visiting

            for nei in ajd[node]:
                if not dfs(nei):
                    return False
            states[node] = visited
            res.append(node)
            return True
 

        for nodes in ajd:
            if not dfs(nodes):
                return []

        return res
