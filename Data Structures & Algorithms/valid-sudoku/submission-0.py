class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        sqrs = {}
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    if str(i) not in rows:
                        rows[str(i)] = []
                    if str(j) not in cols:
                        cols[str(j)] = []
                    sqr_ind = (str(f"{    (i//3)  +1  }{  (j//3)  +1}"))
                    if sqr_ind not in sqrs:
                        sqrs[sqr_ind] = []

                    if board[i][j] in rows[str(i)] or board[i][j] in cols[str(j)] or board[i][j] in sqrs[sqr_ind]:
                        return False
                    rows[str(i)].append(board[i][j])
                    cols[str(j)].append(board[i][j])
                    sqrs[str(f"{    (i//3)  +1  }{  (j//3)  +1   }")].append(board[i][j])
        return True

            
            
            

        # need to remove "." from rows, cols, and squares
    