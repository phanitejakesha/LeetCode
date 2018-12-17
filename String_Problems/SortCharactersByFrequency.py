#Leetcode problem Number 451
#Sort Characters By Frequency
#Autgor: Phani Teja Kesha

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter 
        alphaCount = Counter(s)
        listValues = sorted(alphaCount.keys(),key = lambda x:alphaCount[x],reverse = True)
        ans = []
        for i in listValues:
            ans.append(i*alphaCount[i])
        return ''.join(ans)
