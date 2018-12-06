#Leetcode problem Number 228
#Summary ranges

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        ans =[]
        boo = False
        lastInt = -10000000
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1] and boo == False:
                firstInt = nums[i]
                lastInt = nums[i+1]
                boo = True
            elif nums[i]+1==nums[i+1] and boo == True:
                lastInt = nums[i+1]
            else:
                if lastInt == -10000000:
                    ans.append(str(nums[i]))
                else:
                    ans.append(str(firstInt)+"->"+str(lastInt))
                    lastInt = -10000000
                    boo = False
            print(ans)
        if boo == True:
            ans.append(str(firstInt)+"->"+str(nums[i+1]))
        else:  
            ans.append(str(nums[i+1]))
        return ans
                
            
                        
        
