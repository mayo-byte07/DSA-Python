class Solution(object):
    def isValidSudoku(self, board):
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                if val != '.':
                    # Create unique representations for rows, columns, and 3x3 boxes
                    row_val = (r, val)
                    col_val = (val, c)
                    box_val = (r // 3, c // 3, val)
                    
                    if row_val in seen or col_val in seen or box_val in seen:
                        return False
                        
                    seen.add(row_val)
                    seen.add(col_val)
                    seen.add(box_val)
                    
        return True