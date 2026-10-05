class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols = len(board), len(board[0])

        # rows
        for r in range(rows):
            s = set()
            for c in range(cols):
                if board[r][c] in s:
                    return False
                elif board[r][c] is not '.':
                    s.add(board[r][c])

        #cols

        for r in range(rows):
            s = set()
            for c in range(cols):
                if board[c][r] in s:
                    return False
                elif board[c][r] is not '.':
                    s.add(board[c][r])

        # 3by3 grid

        starts = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
        for i,j in starts:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item is not '.':
                        s.add(item)



        return True