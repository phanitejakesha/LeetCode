#Leetcode problem Number 961
#N repaeted elements in 2N array
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        numberHash = set()
        for i in range(0,len(A)):
            if A[i] in numberHash:
                return A[i]
            else:
                numberHash.add(A[i])
        
