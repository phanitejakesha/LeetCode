class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                xor = nums[i]^nums[j]
                if xor>maxVal:
                    maxVal = xor
        return maxVal
