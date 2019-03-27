class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = list(str(num))
        maxVal = num
        for i in range(0,len(x)):
            for j in range(i+1,len(x)):
                temp1  = x[i]
                temp2  = x[j]
                x[j] = temp1
                x[i] = temp2
                val = int(''.join(x))
                if val>maxVal:
                    maxVal = val
                x[j] = temp2
                x[i] = temp1
        return maxVal
                
        
        
