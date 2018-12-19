#Leetcode problem Number 20
#valid Parenthesis

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li=[]
        if len(s)%2!=0:
            return False
        for i in range(0,len(s)):
            if s[i]=='[' or s[i]=='{' or s[i]=='(':
                li.append(s[i])
            elif s[i]==']':
                if len(li)==0:
                     return False
                ele=li.pop()
                if ele!='[':
                    return False
            elif s[i]==')':
                if len(li)==0:
                    return False
                ele=li.pop()
                if ele!='(':
                    return False
            elif s[i]=='}':
                if len(li)==0:
                    return False
                ele=li.pop()
                if ele!='{':
                    return False
        if len(li)==0:
            return True
        else:
            return False
                
                
        
