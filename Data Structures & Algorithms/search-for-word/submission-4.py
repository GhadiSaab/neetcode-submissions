class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c, i):
            if i == n: return True

            if  r<0 or r>= rows or c >= cols or c<0 or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = '#'
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                if dfs(nr,nc,i+1):
                    return True

            board[r][c] = temp
            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True


        return False

              