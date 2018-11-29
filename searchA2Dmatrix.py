#Leetcode problem Number 74
#Search a 2d Matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in range(0,len(matrix)):
            if len(matrix[i])>0:
                if matrix[i][0]>target or matrix[i][len(matrix[i])-1]<target:
                    continue
                else:
                    for j in range(0,len(matrix[i])):
                        if matrix[i][j]==target:
                            return True
        return False
