class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges)+1)]
        size = [1] * (len(edges)+1)
        res = []

        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(a,b): 
            na,nb = find(a), find(b)
            if na == nb:
                res.append([a,b])
                return False

            if size[na] < size[nb]:
                na,nb = nb,na

            parents[nb] = na
            size[na] += size[nb]
            return True

        
        for u,v in edges:
            union(u,v)

        return res[-1]
