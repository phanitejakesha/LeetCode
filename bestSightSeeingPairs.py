class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        profitDictI  = []
        profitDictJ  = []
        
        #Thinking this as Profit I 
        for i in range(0,len(A)):
            profitDictI.append(A[i]+i)
                    
        #Thinking this as Profit J 
        for j in range(0,len(A)):
            profitDictJ.append(A[j]-j)
            
        maxVal = -1
        for k in range(len(A)-1,-1,-1):
            if profitDictJ[k] >maxVal:
                maxVal = profitDictJ[k]
            else:
                profitDictJ[k] = maxVal
        ans = -1
        for m in range(0,len(A)-1):
            if profitDictI[m]+ profitDictJ[m+1] > ans:
                ans = profitDictI[m]+ profitDictJ[m+1]
        return ans
            
            
            
            
            
            
#         i = 0
#         j = i+1
#         maxVal = -1
#         index = -1
        
        
        
        
        
        
        
#         while i!= len(profitDictI):
#             if maxVal == -1:
#                 for k in range(j,len(profitDictJ)):
#                     if profitDict[j]>maxVal:
#                         maxVal = profitDict[j]
#                         index = j
#                     elif 
                        
            
            
        
        return 0 
        
               
            
        
