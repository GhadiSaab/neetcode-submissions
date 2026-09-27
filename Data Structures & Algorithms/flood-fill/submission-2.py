class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows,cols = len(image),len(image[0])
        visited = set()
        orr = image[sr][sc]

        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or image[r][c] != orr or (r,c) in visited:
                return

            visited.add((r,c))
            if image[r][c] == orr:
                image[r][c] = color

            dfs(r-1,c) 
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)


        dfs(sr,sc)

        return image