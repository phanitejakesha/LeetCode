#Leetcode problem Number 744
#Find Smallest Letter Greater Than Target

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        from collections import Counter
        letterDict = Counter(letters)
        minVal = 97
        maxVal = 122
        targetVal = ord(target)
        val = targetVal
        while val<=124 and val>=97:
            if val == targetVal:
                val+=1
            if val>122:
                val = 97
            if chr(val) in letterDict:
                return chr(val)
            else:
                val+=1
