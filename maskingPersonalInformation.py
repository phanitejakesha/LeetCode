#Leetcode problem Number 831
#Masking Personal Information

import re

class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        li = [0,1,2,3,4,5,6,7,8,9]
        for i in range(0,len(S)):
            if S[i]=='@':
                count = 1
                pos = i 
                break
            else:
                count = 0
        if count==1:
            S = S.lower()
            return S[0]+5*"*"+S[pos-1]+S[pos:]
        else:
            num = "".join(list(filter(str.isdigit,S)))
            if len(num)==10:
                return "***-***-"+num[6:]
            else:
                x = len(num)-10
                st = "+"+x*"*"+"-"
                return st+"***-***-"+num[len(num)-4:]
