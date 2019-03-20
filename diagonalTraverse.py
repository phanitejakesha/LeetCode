class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        if matrix[0]==[]:
            return []
        if len(matrix)==1:
            return matrix[0]
        i = 0 
        j = 0 
        M = len(matrix)
        N = len(matrix[0])
        ans = []
        boo = True
        while (j!=N-1):
            if j == 0 and i == 0:
                ans.append(matrix[0][0])
            else:
                ans = ans + self.helper1(matrix,i,j,boo)
                boo = not boo
            j+=1     
        while (i!=M):
            ans = ans + self.helper2(matrix,i,j,boo)
            boo = not boo
            i+=1
        return ans       
    def helper1(self,matrix,i,j,boo):
        pRes = []
        while  i!=len(matrix) and j>=0:
            print(i,j)
            pRes.append(matrix[i][j])
            j-=1
            i+=1
        if boo == True:
            return pRes
        return pRes[::-1]
    
    def helper2(self,matrix,i,j,boo):
        pRes = []
        while i!=len(matrix) and j>=0:
            pRes.append(matrix[i][j])
            j-=1
            i+=1
        if boo == True:
            return pRes
        return pRes[::-1]
    
    
        
