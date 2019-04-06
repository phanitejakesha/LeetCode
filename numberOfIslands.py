def gridChanger(grid,i,j):
        if grid[i][j]=='1':
            grid[i][j]='2'
            gridChanger(grid,i-1,j) if i>0 else None
            gridChanger(grid,i,j-1) if j>0 else None
            gridChanger(grid,i+1,j) if i<len(grid)-1 else None
            gridChanger(grid,i,j+1) if j<len(grid[0])-1 else None
        
        else:
            return 
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j]=='1':
                    gridChanger(grid,i,j)
                    count+=1
        return count
                
