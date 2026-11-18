class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = dict()

        for i in range(3):
            for j in range(3):
                squares[(i, j)] = set()

        for row in range(9):
            for col in range(9):

                val = board[row][col]

                if val != ".":

                    if val in rows[col] or val in cols[row] or val in squares[(row//3, col//3)]:
                        return False

                    rows[col].add(val)
                    cols[row].add(val)
                    squares[(row//3, col//3)].add(val)

        return True

        