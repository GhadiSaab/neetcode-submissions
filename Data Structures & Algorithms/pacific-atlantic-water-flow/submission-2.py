class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        res = []
        rows,cols = len(heights), len(heights[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]


        def dfs(r,c,visited,pr,pc):
            if r<0 or r==rows or c<0 or c==cols or (r,c) in visited or heights[r][c] < heights[pr][pc]:
                return 

            visited.add((r,c))

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                dfs(nr,nc,visited,r,c)


        for r in range(rows):
            dfs(r,0,pac,r,0)
            dfs(r,cols-1,atl,r,cols-1)

        for c in range(cols):
            dfs(0,c,pac,0,c)
            dfs(rows-1,c,atl,rows-1,c)

        for (r,c) in pac:
            if (r,c) in atl:
                res.append([r,c])

        
        return res