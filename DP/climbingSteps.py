#Leetcode Question Number 70
#Climbing stairs

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.globalArr = {}
        self.globalArr[1]=1
        self.globalArr[2]=2
        return self.helper(n)
        
        
    def helper(self,n):
        
        if n in self.globalArr:
            return self.globalArr[n]
        else:
            self.globalArr[n] = self.helper(n-1)+self.helper(n-2)
            return self.globalArr[n]
