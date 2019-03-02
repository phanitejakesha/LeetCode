#Pascals Triangle 2

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        res = [[1],[1,1]]
        numRows = rowIndex+2
        if numRows == 2:
            return res
        while numRows!=2:
            l = len(res[len(res)-1])
            midAns = [1]
            for i in range(0,l-1):
                midAns.append(res[len(res)-1][i]+res[len(res)-1][i+1])
            midAns.append(1)
            res.append(midAns)
            numRows-=1
        return res[len(res)-2]
