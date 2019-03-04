#Leetcode
#Author: Phani Teja Kesha
#Is a number happy or not

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x= str(n)
        repeatedSet = set()
        while x!='1':            
            if x in repeatedSet:
                return False
            else:
                repeatedSet.add(x)
            s = 0
            for i in range(0,len(x)):
                s = s + int(x[i])*int(x[i])
            x = str(s)
        return True
                
