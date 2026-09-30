class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        parents = [i for i in range(n)] 
        size = [1] * n

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x


        def union(a,b):
            na,nb = find(a), find(b)
            if na == nb: 
                return False
            if size[na] < size[nb]:
                na,nb = nb,na
            parents[nb] = na
            size[na] += size[nb]
            return True

        count = n
        for u,v in edges:
            if union(u,v):
                count -= 1


        return count == 1 