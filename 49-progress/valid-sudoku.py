from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9x9
        # row 1 - 9 no rep
        for row in board:
            if not self.is_valid(row):
                return False


        # column 1 - 9 no rep
        for i in range(9):
            column = [board[j][i] for j in range(9)]
            if not self.is_valid(column):
                return False


        # sub-boxes 3x3 1 - 9 no rep
        # get 3 rows and 3 columns
        for i in range(3):
            for j in range(3):
                box = self.get_sub_box(board, i, j)
                if not self.is_valid(box):
                    return False

        return True
    
    def get_sub_box(self, board, i, j):
        box = []
        for k in range(3):
            for l in range(3):
                box.append(board[3 * i + k][3 * j + l])
        return box


    def is_valid(self, row):
        row = [cell for cell in row if cell != '.'] # remove empty once
        return len(row) == len(set(row)) # check if there is rep




if __name__ == '__main__':
    board =[["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board))