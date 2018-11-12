#Leetcode problem Number 303
#Raneg Sum Query - Immutable

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.d = {}

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        st = str(str(i)+str(j))
        if st in self.d:
            return self.d[st]
        else:
            s = sum(self.nums[i:j+1])
            self.d[st]=s
            return s
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
