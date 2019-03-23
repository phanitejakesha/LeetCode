class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)==0:
            return nums
        if len(nums[0])==0:
            return nums
        if len(nums)*len(nums[0])!=r*c:
            return nums
        else:
            tempMatrix = [[0]*c]*r
            ans = []
            tempAr = []
            for i in range(0,len(nums)):
                for j in range(0,len(nums[0])):
                    tempAr.append(nums[i][j])
            k = 0
            for i in range(0,len(tempMatrix)):
                parRe = []
                for j in range(0,len(tempMatrix[0])):
                    parRe.append(tempAr[k])
                    k+=1
                ans.append(parRe)
            return ans
                    

        
