#Leetcode problem Number 75
#Sort Colours

"""
Author: Phani Teja Kesha
"""
#Counting sort 
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from collections import Counter 
        d = Counter(nums)
        i= 0
        for key in d:
            val = d[key]
            for j in range(0,val):
                nums[i]=key
                i+=1
        return 
        
        
