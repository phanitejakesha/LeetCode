class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        self.flag = True
        self.count = 0
        if len(A)==0:
            return 0
        for i in range(0,len(A)):
            for j in range(0,len(A[0])):
                if A[i][j]==1:
                    self.helper(A,i,j)
                    if self.flag == True:
                        self.helper1(A,i,j)
                self.flag = True
        return self.count


    def helper(self,board,i,j):
        if board[i][j]==1:
            board[i][j]=2
            a = self.helper(board,i-1,j) if i>0 else False
            b = self.helper(board,i,j-1) if j>0 else False
            c = self.helper(board,i+1,j) if i<len(board)-1 else False
            d = self.helper(board,i,j+1) if j< len(board[0])-1 else False
            if a==False or b==False or c==False or  d==False:
                self.flag = False
        else:
            return True
    
    def helper1(self,board,i,j):
        if board[i][j]==2:
            board[i][j]=3
            self.count+=1
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
