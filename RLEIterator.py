#Leetcode problem Number 900
#RLE Iterator

"""
Author: Phani Teja Kesha
"""

class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.li = A
        return 
    
    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n>0:
            if len(self.li)==0:
                return -1
            if self.li[0]<n:
                n = n - self.li[0]
                self.li= self.li[2:]
            elif self.li[0]==n:
                eleVal= self.li[1]
                self.li = self.li[2:]
                return eleVal
            else:
                self.li[0]=self.li[0]-n
                return self.li[1]
                

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
