class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter 
        liNums = Counter(nums)
        sorted_x = sorted(liNums.items(), key=lambda kv: kv[1],reverse = True)
        ans = []
        for i in range(0,k):
            ans.append(sorted_x[i][0])
        return ans
        
