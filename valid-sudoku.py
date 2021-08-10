class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # n = len of board
        # time: O(n ** 3) -> iterating through n * n grid, each check takes n time
        # space: O(1) -> no extra storage needed
        def checkSquare(row, col, val, board):
            squareRow = row // 3 * 3
            squareCol = col // 3 * 3
            for i in range(3):
                for j in range(3):
                    if board[squareRow + i][squareCol + j] == val and squareRow + i != row and squareCol + j != col:
                        print('found square not righ')
                        return False
            return True

        def checkRow(row, col, val, board):
            for i in range(9):
                if board[row][i] == val and col != i:
                    return False
            return True

        def checkCol(row, col, val, board):
            for i in range(9):
                if board[i][col] == val and row != i:
                    return False
            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.' and \
                    not all((checkSquare(row, col, board[row][col], board),
                             checkRow(row, col, board[row][col], board),
                             checkCol(row, col, board[row][col], board))):
                    return False
        return True
