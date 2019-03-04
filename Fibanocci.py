class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0 :
            return 0
        if N == 1:
            return 1 
        if N == 2:
            return 1
        f0 = 0
        f1 = 1
        i = 2
        while N+1!=i:
            f2 = f1 + f0
            f0 = f1
            f1 = f2
            i= i + 1
        return f1
