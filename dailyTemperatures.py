#Leetcode problem Number 739
#Daily Temperatures

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        ansLi = [0 for x in range(0,len(temperatures))]
        li = []
        li.append((temperatures[0],0))        
        for i in range(1,len(temperatures)):
            while li and temperatures[i]>li[-1][0]:
                ansLi[li[-1][1]]=abs(li[-1][1]-i)
                li.pop()
                # if len(li) == 0:
                    # break
            li.append((temperatures[i],i))
        return ansLi
                
