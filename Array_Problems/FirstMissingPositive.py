#Leetcode problem Number 41
#First Missing positive

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      
        d = {}
        for i in range(0,len(nums)):
            d[nums[i]]=1
        for i in range(1,len(nums)+1):
            if i in d:
                continue
            else:x
                return i
        return len(nums)+1
