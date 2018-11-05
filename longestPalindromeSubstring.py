#Leetcode number 5
#Longest palindromic substring
"""
Author: Phani Teja Kesha
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        ans = 0
        st = ""
        for i in range(0,2*n-1):
            left = i//2
            right = left+i%2
            while left>=0 and right<n and s[left]==s[right]:
                    if len(s[left:right+1])>ans:
                        ans=len(s[left:right+1])
                        st = s[left:right+1]
                    left-=1
                    right+=1
        return st
