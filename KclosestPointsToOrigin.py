#Leetcode problem Number 973
#K closest points to origin 

"""
Author: Phani Teja Kesha
"""

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        ans =  []
        disVal = []
        for i in points:
            d = i[0]*i[0] + i[1]*i[1]
            disVal.append(d)
        Z = [x for _,x in sorted(zip(disVal,points))]
        return Z[:K]
        
