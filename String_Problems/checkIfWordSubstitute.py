class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        if len(S)<3:
            return False
        stac = []
        for i in range(0,len(S)):
            stac.append(S[i])
            if len(stac)>=3:
                if stac[len(stac)-1] == 'c' and stac[len(stac)-2]=='b' and stac[len(stac)-3]=='a':
                    stac = stac[:len(stac)-3]
        if len(stac)==0:
            return True
        if len(stac)>3:
            return False
        if len(stac)<3:
            return False
        if stac[len(stac)-1] == 'c' and stac[len(stac)-2]=='b' and stac[len(stac)-3]=='a':
            return True
        return False
