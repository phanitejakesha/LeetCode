#Leetcode problem Number 941
#Valid Mountain Array

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A)<3:
            return False
        decFlag = True
        incFlag = False
        for i in range(0,len(A)-1):
            #print(A[i],A[i+1])
            if A[i]<A[i+1]: 
                incFlag = True
                if decFlag == False:
                    return False
            elif A[i]>A[i+1]:
                decFlag = False 
            else:
                return False
        if decFlag==False and incFlag ==True:
            return True
        else:
            return False
        
