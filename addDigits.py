class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        if len(s)==1:
            return int(s)
        while len(s)!=1:
            parSum = 0
            for i in range(0,len(s)):
                parSum = parSum + int(s[i])
            s = str(parSum)
        return int(s)
