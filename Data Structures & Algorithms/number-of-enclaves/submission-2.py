class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        land, borderland = 0,0
        visited = set()

        # our dfs function should return 1 if the land is connected to a border and 0 if not
        def dfs(r,c):
            if r < 0 or r ==rows or c<0 or c==cols or grid[r][c] == 0 or (r,c) in visited: 
                return 0

            visited.add((r,c))
            count = 1
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                count += dfs(nr,nc)

            return count

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    land += 1


        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    borderland += dfs(r,c)


        return land - borderland