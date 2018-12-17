#Leetcode problem Number 944
#delete column to make sorted

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if len(A)==0:
            return 0
        ans = 0
        for i in range(0,len(A[0])):
            st = ""
            for j in range(0,len(A)):
                st = st + A[j][i]
            if self.isInAlphabeticalOrder(st) is False:
                ans+=1
        return ans
            
        
    def isInAlphabeticalOrder(self,word):
        return word==''.join(sorted(word))
