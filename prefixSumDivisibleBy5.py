class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = []
        ans = 0
	#This is equal to right shift of a binary string
        for i in range(0,len(A)):
            ans  = ans * 2
            ans = ans + A[i]
            if ans%5==0:
                result.append(True)
            else:
                result.append(False)
        return result
        
