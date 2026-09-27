class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        count = 0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c >= cols or grid[r][c] == 0:
                return 

            grid[r][c] = 0

            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                dr = r + dr
                dc = c + dc 
                dfs(dr,dc)

        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and grid[r][c] == 1:
                    dfs(r,c)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    count += 1 


                            

        return count 