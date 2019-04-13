class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        perimeter = 0 
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                neighbor = 0
                if grid[i][j]==1:
                    #the island has started 
                    if i>0 and grid[i-1][j]==1:
                        neighbor+=1
                    if j>0 and grid[i][j-1]==1:
                        neighbor+=1
                    if i<len(grid)-1 and grid[i+1][j]==1:
                        neighbor+=1
                    if j<len(grid[0])-1 and grid[i][j+1]==1:
                        neighbor+=1
                    if neighbor==4:
                        perimeter+=0
                    elif neighbor==3:
                        perimeter+=1
                    elif neighbor==2:
                        perimeter+=2
                    elif neighbor==1:
                        perimeter+=3
                    elif neighbor==0:
                        perimeter+=4
        return perimeter
                    
                        
                    
