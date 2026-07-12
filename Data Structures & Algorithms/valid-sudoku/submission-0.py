class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        sub_box = {}
        cols = {}

        for rowIndex in range(len(board)):
            row = board[rowIndex]
            if not rowIndex in rows:
                rows[rowIndex] = set()

            for colIndex in range(len(row)):
                col = row[colIndex]
                if not colIndex in cols:
                    cols[colIndex] = set()

                if not col.isnumeric():
                    continue

                if col in cols[colIndex]:
                    return False
                else:
                    cols[colIndex].add(col)
                
                if col in rows[rowIndex]:
                    return False
                else:
                    rows[rowIndex].add(col)

                subBoxIndex = (rowIndex // 3) * 3 + (colIndex // 3)
                if not subBoxIndex in sub_box:
                    sub_box[subBoxIndex] = set()

                if col in sub_box[subBoxIndex]:
                    return False
                else:
                    sub_box[subBoxIndex].add(col)        
                
        return True