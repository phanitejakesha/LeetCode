class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        firstSeen = -1
        for i in range(0,len(nums)):
            if nums[i]==target:
                firstSeen=i
                break
        
        lastSeen = -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                lastSeen = i
                break
        return [firstSeen,lastSeen]
        
