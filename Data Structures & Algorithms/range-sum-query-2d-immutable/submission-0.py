class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = [[0]*(col + 1) for _ in range(row + 1)]
        for r in range(row):
            for c in range(col):
                self.prefix[r+1][c+1] = (
                            matrix[r][c]               #Current
                            + self.prefix[r][c+1]      # TOP
                            + self.prefix[r+1][c]      # LEFT
                            - self.prefix[r][c]        # TOP-LEFT overlap
                        )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.prefix[row2+1][col2+1] # bottom
                - self.prefix[row1][col2+1] # top
                - self.prefix[row2+1][col1] #left
                + self.prefix[row1][col1] # overlap
        )
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)