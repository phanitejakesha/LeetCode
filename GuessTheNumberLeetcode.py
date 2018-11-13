#Leetcode problem Number 374
#Guess the number lower or higher

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        high = n
        while high>=i:
            mid = i + (high-i)//2
            if guess(mid)>0:
                i = mid+1
            elif guess(mid)<0:
                high = mid-1
            else:
                return mid
        return -1
        
