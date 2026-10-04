from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        place = 0
        rows, cols = len(grid), len(grid[0])
        inf = 2147483647
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        
        while q:
            place += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr < rows and nr >= 0 and nc >= 0 and nc < cols and grid[nr][nc] == inf:
                        q.append((nr,nc))
                        grid[nr][nc] = place
                    

        
                        



