class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        available = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    available.add((r,c))

        def dfs(r,c):
            if r<0 or r==rows or c<0 or c==cols or board[r][c] == 'X' or (r,c) not in available:
                return

            available.discard((r,c))
            for dr,dc in directions:
                dfs(r+dr,c+dc)
             

        for r in range(rows):
            for c in range(cols):
                if (r==0 or r==rows-1 or c== 0 or c == cols-1) and (board[r][c] == 'O' and (r,c) in available):
                    dfs(r,c)

        for r,c in available:
            board[r][c] = 'X'