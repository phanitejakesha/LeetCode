class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Dynamic Programming solution
        dp = [[0]*n]*m
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 or j==n-1:
                    dp[i][j]=1
                else:
                    dp[i][j]= dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
        
    
def recursiveSolution():
    self.count=0
    self.helper(0,0,m,n)
    return self.count
                
def helper(self,i,j,m,n):
    if i<m-1:
        self.helper(i+1,j,m,n)
    if j<n-1:
        self.helper(i,j+1,m,n)
    if i==m-1 and j==n-1:
        self.count+=1
    return None




