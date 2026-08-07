class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value==".":
                    continue
                box_index = (r // 3) * 3 + (c // 3)
                row_tag= (value,"row",r)
                col_tag=(value,"col",c)
                box_tag=(value,"box",box_index)
                if row_tag in seen or col_tag in seen or box_tag in seen:
                    return False
                else:
                    seen.add(row_tag)
                    seen.add(col_tag)
                    seen.add(box_tag)
        return True
                
        