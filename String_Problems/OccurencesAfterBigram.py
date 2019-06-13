#
# Author: Phani Teja Kesha
#
class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        ans = []
        listString = text.split(' ')
        for i in range(0,len(listString)-2):
            if (listString[i]==first) and (listString[i+1]==second):
                ans.append(listString[i+2])
        return ans
                
        
