class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c == 0 or c == 1 or c == 2:
            return True
        i = 1
        while i < (c//2)+1:
            x = i*i 
            midX = c-x
            if midX<0:
                break
            y = (c-x)**0.5
            if (int(y)-y)==0:
                return True
            i+=1
        return False
        
        
