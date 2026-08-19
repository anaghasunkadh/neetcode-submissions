class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hasshet=set()
        for r in range(9):
            for c in range(9):
                value=board[r][c]
                if value==".":
                    continue
                box=3*(r//3)+(c//3)
                row_tag=("row",value,r)
                col_tag=("col",value,c)
                boxi=("box",value,box)
                if row_tag  in hasshet or col_tag  in hasshet or boxi  in hasshet:
                    return False
                else:
                    hasshet.add(row_tag)
                    hasshet.add(col_tag)
                    hasshet.add(boxi)
        return True

        