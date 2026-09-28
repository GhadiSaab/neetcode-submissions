from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        inf = 2147483647
        count = 1 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = dr+r, dc+c
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == inf:
                        grid[nr][nc] = count 
                        q.append((nr,nc))

            count += 1

