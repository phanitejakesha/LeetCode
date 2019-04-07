class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        maxArea = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]==1:
                    d = gridChanger(grid,i,j)
                    if maxArea < d:
                        maxArea = d
        return maxArea
    
def gridChanger(grid,i,j):
        if grid[i][j]==1:
            grid[i][j]=2
            if i>0:
                q = gridChanger(grid,i-1,j)
            else:
                q = 0
            if j>0:
                w = gridChanger(grid,i,j-1)
            else:
                w = 0
                
            if i<len(grid)-1:
                e = gridChanger(grid,i+1,j)
            else:
                e = 0
                
            if j<len(grid[0])-1:
                r = gridChanger(grid,i,j+1)
            else:
                r = 0    
            return 1 + q+w+e+r
        else:
            return 0
        
