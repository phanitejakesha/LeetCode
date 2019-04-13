#Leetcode problem Number 338
#Couting Bits
#Dynamic Programming
#Author : Phani Teja

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num==1:
            return [0,1]
        else:
            dp = [0]*(num+1)
            dp[0]=0
            dp[1]=1
            mostRecentPower = 1
            for i in range(2,num+1):
                #Check if its power of 2 directly 
                if mostRecentPower*2 == i:
                    mostRecentPower = i
                    dp[i]=1
                else:
                    dp[i]=dp[mostRecentPower]+dp[i-mostRecentPower]
        return dp
                
        
