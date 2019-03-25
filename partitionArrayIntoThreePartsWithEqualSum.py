class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        totalSum  = sum(A)
        parSum = totalSum%3
        if parSum != 0:
            return False
        else:
            pSum  = totalSum // 3
            s = 0 
            count = 0
            for i in range(0,len(A)):
                if s==pSum:
                    s  = A[i]
                    count+=1
                else:
                    s = s + A[i]
            if s == pSum:
                count+=1
            if count == 3:
                return True
            return False
                
        
