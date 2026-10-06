class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            nx, ny = find(x), find(y)
            if nx == ny:
                return False

            if rank[nx] < rank[ny]:
                nx, ny = ny, nx

            parent[ny] = nx
            rank[nx] += rank[ny]
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]