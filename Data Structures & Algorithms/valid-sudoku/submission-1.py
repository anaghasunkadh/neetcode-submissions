class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen=set()
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value==".":
                    continue
                boxi=3*(r//3)+(c//3)
                row_tag=(r,"row",value)
                col_tag=(c,"col",value)
                box_tag=(boxi,"box",value)
                if row_tag in seen or col_tag in seen or box_tag in seen:
                    return False
                else:
                    seen.add(row_tag)
                    seen.add(col_tag)
                    seen.add(box_tag)
        return True



        