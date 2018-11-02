#sliding window maximum
#leetcode 239

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        if nums==[]:
            return []
        for i in range(0,len(nums)-k+1):
            if i == 0:
                prevMax = max(nums[i:i+k])
                ans.append(prevMax)
            else:
                if prevMax == nums[i-1]:
                    prevMax = max(nums[i:i+k])
                    ans.append(prevMax)
                else:
                    if prevMax > nums[i+k-1]:
                        print(nums[i+k-1])
                        ans.append(prevMax)
                    else:
                        prevMax = nums[i+k-1]
                        ans.append(nums[i+k-1])
        return ans 
                    
