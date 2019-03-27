class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        ans = 0
        count = 1
        for i in range(0,len(nums)-1):
            if nums[i] < nums[i+1] :
                count+=1
            else:
                if ans < count:
                    ans = count
                count = 1 
                    
        if ans < count:
            ans = count
            count = 1 
        return ans

