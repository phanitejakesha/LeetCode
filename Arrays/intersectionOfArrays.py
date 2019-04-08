class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans = []
        for key in c1:
            if key in c2:
                #intersection found, check the min number and replicate 
                subInter = [key]*min(c1[key],c2[key])
                ans+=subInter
        return ans
            
        
        
