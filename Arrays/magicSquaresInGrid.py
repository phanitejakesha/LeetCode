class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        if len(grid)<3 or len(grid[0])<3:
            return 0
        answer = 0 
        for i in range(0,len(grid)-2):
            for j in range(0,len(grid[0])-2):
                if checkGrid(grid,i,j):
                    answer+=1
        return answer


def checkGrid(grid,i,j):
    flagValue = True
    a,b,c,d,e,f,g,h,i = grid[i][j],grid[i][j+1],grid[i][j+2],         grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]
    if a+b+c==d+e+f==g+h+i==a+d+g==b+e+h==c+f+i==a+e+i==c+e+g:
        flagValue = True
    else:
        flagValue = False
    setOfValues = set([a,b,c,d,e,f,g,h,i])
    for i in range(1,10):
        if i not in setOfValues:
            flagValue = False
    return flagValue
            
        
    
    
                
        
