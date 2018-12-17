#Leetcode problem Number 942
#DI String Match

class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        iVal = 0
        dVal = len(S)
        ans = []
        for i in S:
            if i=='I':
                ans.append(iVal)
                iVal+=1
            else:
                ans.append(dVal)
                dVal-=1
        ans.append(dVal)
        return ans
        
