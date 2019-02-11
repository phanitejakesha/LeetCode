#Leetcode problem Number 989
#Add to array form of integers

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        ans = []
        kList = list(str(K))
        B = []
        for i in kList:
            B.append(int(i))
        length = max(len(A),len(B))
        if len(A)!=length:
            d = length - len(A)
            re = [0]*d
            A = re + A
        if len(B)!=length:
            d = length - len(B)
            re = [0]*d
            B = re + B
        c = 0 
        for i in range(len(A)-1,-1,-1):
            redSum = A[i] + B[i] + c 
            s = redSum % 10 
            c = redSum // 10 
            if s>9:
                redAns = list(str(s))
                for j in range(len(redAns)-1,-1,-1):
                    ans.insert(0,int(j))
            else:   
                ans.insert(0,s)
        if c!=0:
            ans.insert(0,c)
        return ans
