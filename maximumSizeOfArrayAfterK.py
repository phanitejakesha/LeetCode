class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        from collections import Counter
        li = Counter(A)
        val = li.keys()
        val.sort()
        i = 0
        while K!=0:
            if val[i]<0:
                K-=li[val[i]]
                if abs(val[i]) in li:
                    li[abs(val[i])]+=li[val[i]]
                else:
                    li[abs(val[i])]=li[val[i]]
                if K>=0:
                    del li[val[i]]
                i+=1
            else:
                K=K%2
                if K == 1:
                    numVal = val[i]
                    li[val[i]]-=1
                    if val[i]*-1 in li:
                        li[val[i]*-1]+=1
                    else:
                        li[val[i]*-1]=1
                    K=0
        ans = 0
        for key in li:
            ans = ans + key*li[key]
        return ans
                    
                    
                
                

                    
                    
                
                
                
                
            
            
            
