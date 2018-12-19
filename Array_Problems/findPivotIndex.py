#leetcode problem number 724
#Find pivot index
#Author: Phani Teja kesha

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        leftVal = sum(nums[:i-1])
        rightVal = sum(nums[i:])
        while i<=len(nums):
            if leftVal==rightVal:
                return i-1
            leftVal = leftVal + nums[i-1]
            if i<len(nums):
                rightVal = rightVal -nums[i]
            i+=1
        return -1
