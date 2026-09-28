class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row , col = len(board), len(board[0])
        # checking row wise 
        for r in range(row):
            seen = set()
            for c in range(col):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # checking col wise 
        for c in range(col):
            seen = set()
            for r in range(row):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        for r in range(0,9,3):
            for c in range(0,9,3):
                seen = set()
                for b_r in range(r,r+3):
                    for b_c in range(c, c+3):
                        if board[b_r][b_c] == ".":
                            continue
                        if board[b_r][b_c] in seen:
                            return False
                        seen.add(board[b_r][b_c])
        return True
                