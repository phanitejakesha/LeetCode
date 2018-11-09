#Leetcode problem Number 453
#Minimum moves to equal an array

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        m = min(nums)
        return s-len(nums)*m
