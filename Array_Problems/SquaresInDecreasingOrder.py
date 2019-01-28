#Leetcode problem Number 977
#Squares in decreasing order

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ansLi = []
        for i in A:
            ansLi.append(i*i)
        ansLi.sort()
        return ansLi
        
        
