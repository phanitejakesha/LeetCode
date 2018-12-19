#leetcode problem number 946
#Validate stack sequence
"""
Author: Phani Teja Kesha
"""

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i = 0
        j = 0
        presentStack = []
        while i<len(pushed):
            #print(popped[j],pushed[i])
            if popped[j]!=pushed[i]:
                if len(presentStack)==0:
                    presentStack.append(pushed[i])
                else:
                    if presentStack[-1]!=popped[j]:
                        presentStack.append(pushed[i])
                    else:
                        presentStack.pop()
                        i-=1
                        j+=1
            else:
                j+=1
            i+=1
            #print(presentStack)
        st1 = popped[j:][::-1]
        st2  = presentStack
        #print(st1,st2)
        if len(st1)!=len(st2):
            return False
        for i in range(0,len(st1)):
            if st1[i]!=st2[i]:
                return False
        return True
                
                
            
