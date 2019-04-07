class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        openB = 0
        closeB = 0
        j = 0 
        stack = []
        for i in range(0,len(S)):
            if S[i]=='(':
                openB +=1
            if S[i]==')':
                closeB+=1
            if openB == closeB:
                stack.append(S[j:i+1])
                j = i +1
        result  = []
        for key in stack:
            if len(key)<2:
                pass
            else:
                result.append(key[1:len(key)-1])
        return ''.join(result)
            
                
