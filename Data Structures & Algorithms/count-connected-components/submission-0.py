class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [1] * n
        count = n

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(a,b):
            na,nb = find(a),find(b)
            if na == nb:
                return False

            if rank[na] < rank[nb]:
                na,nb = nb,na

            parents[nb] = na
            rank[na] += rank[nb]
            return True

        for a,b in edges:
            if union(a,b):
                count -= 1
            
        return count 
