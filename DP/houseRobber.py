#Leetcode problem Number 198
#House robber

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        dp = [0]*len(nums)
        if len(nums)==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        if len(nums)>2:
            for j in range(2,len(nums)):
                dp[j]=max(dp[j-1],nums[j]+dp[j-2])
        return dp[-1]
