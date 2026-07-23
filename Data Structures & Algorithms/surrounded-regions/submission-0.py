class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visisted_set=set()
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        stack=[]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i==0 or i==len(board)-1 or j==0 or j==len(board[i])-1) and board[i][j]=="O":
                        stack.append((i,j))
                        visisted_set.add((i,j))
        while stack:
            row,col=stack.pop()
            for dr,dc in directions:
                nrow=row+dr
                ncol=col+dc
                if 0<=nrow<len(board) and 0<=ncol<len(board[i]) and (nrow,ncol) not in visisted_set and board[nrow][ncol]=="O":
                    stack.append((nrow,ncol))
                    visisted_set.add((nrow,ncol))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=="O" and (i,j) not in visisted_set:
                    board[i][j]="X"
        
                    


                    

        
        