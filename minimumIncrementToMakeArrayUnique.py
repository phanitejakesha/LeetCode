"""
Author: Phani Teja Kesha
"""
#leetcode problem number 945
#minimum increment to make an array unique

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        i = 0
        res = 0
        while i < len(A)-1:
            if A[i]==A[i+1]:
                res = res + 1
                A[i+1]=A[i+1]+1
            elif A[i+1]<A[i]:
                res = res + A[i]+1-A[i+1]
                A[i+1]=A[i]+1
            i+=1
        #print(A)
        return res
        
