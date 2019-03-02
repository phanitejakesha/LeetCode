class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return 
        k = k % len(nums)
        l = len(nums)-1
        for i in range(0,len(nums)//2):
            temp = nums[i]
            nums[i] = nums[l-i]
            nums[l-i] = temp
        for i in range(0,k//2):
            temp = nums[i]
            nums[i] = nums[k-1-i]
            nums[k-1-i] = temp
        for i in range(k,k+(l-k+1)//2):
            temp = nums[i]
            nums[i] = nums[l-i+k]
            nums[l-i+k] = temp
