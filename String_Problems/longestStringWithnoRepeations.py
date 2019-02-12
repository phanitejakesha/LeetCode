#Leetcode problem Number 3
#Longest string without repeating characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordDict = {}
        ans = 0 
        fP = 0 
        res = 0 
        for i in range(0,len(s)):
            if s[i] not in wordDict:
                wordDict[s[i]]=i
                ans= ans + 1
            else:
                if ans> res:
                    res = ans
                sP = wordDict[s[i]] + 1
                for j in range(fP,sP):
                    del wordDict[s[j]]
                wordDict[s[i]]=i
                fP = sP
                ans = len(wordDict)
        if ans> res:
            res = ans 
        return res
                
                
