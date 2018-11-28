#leetcode Problem number 747
#Largest Numberat least twice os numbers


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxVal = max(nums)
        for i in range(0,len(nums)):
            if maxVal == nums[i]:
                ans = i
                continue
            else:
                if 2*nums[i]>maxVal:
                    return -1
        return ans
