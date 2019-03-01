#Pascal's Triangle
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        if numRows ==1:
            return res
        res = [[1],[1,1]]
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
        return res
