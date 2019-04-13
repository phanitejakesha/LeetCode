class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        listNumber = Counter(nums)
        ans = 0
        for key in listNumber:
            if key-1 in listNumber:
                val = listNumber[key] + listNumber[key-1]
                if val > ans:
                    ans = val
            if key+1 in listNumber:
                val = listNumber[key] + listNumber[key-1]
                if val > ans:
                    ans = val
        return ans
                
