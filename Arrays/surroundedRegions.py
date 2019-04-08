class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.flag = True
        if len(board)==0:
            return 0
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if board[i][j]=='O':
                    self.helper(board,i,j)
                    if self.flag == True:
                        self.helper1(board,i,j)
                    else:
                        self.helper2(board,i,j)
                self.flag = True


    def helper(self,board,i,j):
        if board[i][j]=='O':
            board[i][j]='Z'
            a = self.helper(board,i-1,j) if i>0 else False
            b = self.helper(board,i,j-1) if j>0 else False
            c = self.helper(board,i+1,j) if i<len(board)-1 else False
            d = self.helper(board,i,j+1) if j< len(board[0])-1 else False
            if a==False or b==False or c==False or  d==False:
                self.flag = False
        else:
            return True
    
    def helper1(self,board,i,j):
        if board[i][j]=='Z':
            board[i][j]='X'
            self.helper1(board,i-1,j) if i>0 else None
            self.helper1(board,i,j-1) if j>0 else None
            self.helper1(board,i+1,j) if i<len(board)-1 else None
            self.helper1(board,i,j+1) if j< len(board[0])-1 else None
        else:
            return True
    
    def helper2(self,board,i,j):
        if board[i][j]=='Z':
            board[i][j]='O'
            self.helper2(board,i-1,j) if i>0 else None
            self.helper2(board,i,j-1) if j>0 else None
            self.helper2(board,i+1,j) if i<len(board)-1 else None
            self.helper2(board,i,j+1) if j< len(board[0])-1 else None
        else:
            return True
        
#         oxo
#         xox
#         oxo
        
        
        
