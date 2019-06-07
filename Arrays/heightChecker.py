class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        x = sorted(heights)
        result = 0
        for i in range(0,len(x)):  
            if x[i]!=heights[i]:
                result+=1
        return result
            
