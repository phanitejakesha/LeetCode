class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        rankDict = {}
        for i in range(0,len(nums)):
            rankDict[nums[i]] = i 
        ans  = {}
        i = 0 
        for key in sorted(rankDict, reverse = True):
            if i == 0:
                ans[rankDict[key]] = "Gold Medal"
            elif i == 1:
                ans[rankDict[key]]  = "Silver Medal"
            elif i == 2:
                ans[rankDict[key]]  = "Bronze Medal"
            else:
                ans[rankDict[key]] = str(i+1)
            i+=1
        
        res = []
        for key in sorted(ans):
            res.append(ans[key])
        return res
            
                
            
        
