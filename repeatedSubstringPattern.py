class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        repeatedString  = s + s
        for i in range(1,len(repeatedString)-len(s)):
            if repeatedString[i:i+len(s)]==s:
                return True
        return False

