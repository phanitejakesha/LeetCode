#Leetcode problem Number 121
#Best time to buy or sell a stock
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minVal = 999999999
        maxVal = 0;
        for i in range(0,len(prices)):
            if prices[i]<minVal:
                minVal = prices[i]
            if (prices[i]-minVal)>maxVal:
                maxVal = prices[i]-minVal
        return maxVal
                       
                
                    
