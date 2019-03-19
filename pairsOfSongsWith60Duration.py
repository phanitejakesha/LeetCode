class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import Counter
        for i in range(0,len(time)):
            time[i]= time[i]%60
        dCount = {}
        for t in time:
            if t in dCount:
                dCount[t]+=1
            else:
                dCount[t]=1
        ans = 0 
        usedVal = set()
        for key in dCount:
            if key in usedVal:
                continue
            elif key == 0 or key==30:
                usedVal.add(key)
                ans += (dCount[key]*(dCount[key]-1))//2
            elif key!=0 and 60-key in dCount:
                usedVal.add(key)
                usedVal.add(60-key)
                ans += dCount[key]*dCount[60-key]
            
        return ans
                
            
