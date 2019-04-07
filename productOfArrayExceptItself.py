class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """    
        left = 1
        n = len(nums)
        result = []
        for i in range(0,n):
            result.append(left)
            left= left* nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            result[i]= result[i]*right
            right= right* nums[i]
        return result
