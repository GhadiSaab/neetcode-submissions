class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevH):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or (r, c) in visited
                    or heights[r][c] < prevH):
                return
            visited.add((r, c))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        return [list(p) for p in pac & atl]

            
            

