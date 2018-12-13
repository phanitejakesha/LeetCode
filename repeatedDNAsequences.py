#Repeated DNA Sequence
#Leetcode Number 187

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d=set()
        res=set()
        for i in range(0,len(s)-9):
            if s[i:i+10] not in d:
                d[s[i:i+10]]=1
            else:
                if s[i:i+10] not in res:
                    res[s[i:i+10]]=1
        return list(res.keys())
                
        
