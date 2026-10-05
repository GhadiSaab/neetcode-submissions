class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False
        rank = [1] * n
        # building the adj list
        parents = [0] * n
        for i in range(n):
            parents[i] = i


        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x


        def union(x,y):
            nx,ny = find(x), find(y)
            if nx == ny: 
                return False

            if rank[nx] < rank[ny]:
                nx,ny = ny,nx
            parents[ny] = nx
            rank[nx] += rank[ny]


        for u,v in edges:
            if union(u,v) == False:
                return False

        return True
            


