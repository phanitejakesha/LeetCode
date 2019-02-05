#Leetcode problem Number 392
#isSubsequence
#Autgor: Phani Teja Kesha

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        j = 0
        ans = 0
        for i in range(0,len(t)):
            if s[j]==t[i]:
                ans+=1
                j+=1
                if ans == len(s):
                    return True
        if ans == len(s):
            return True
        return False
                
        
