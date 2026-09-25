class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for r in range(row):
            seen = set()
            for c in range(col):
                num = board[r][c]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        for c in range(col):
            seen = set()
            for r in range(row):
                num = board[r][c]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen = set()
                for r in range(box_row, box_row+3):
                    for c in range(box_col, box_col+3):
                        num = board[r][c]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)

        return True
        