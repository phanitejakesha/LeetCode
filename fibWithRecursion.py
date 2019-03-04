class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        return self.helper(N)
     
    def helper(self,N):
        if N == 0:
            return 0
        elif N ==1:
            return 1
        return self.helper(N-1) + self.helper(N-2)
