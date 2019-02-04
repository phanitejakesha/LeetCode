#Leetcode problem Number 985
#Sum of even number after queries

class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        evenSum = 0
        ans = []
        for i in A:
            if i%2==0:
                evenSum = evenSum+i
        for i in range(0,len(queries)):
            targetVal = A[queries[i][1]]
            changedVal = targetVal + queries[i][0]
            A[queries[i][1]]=A[queries[i][1]]+queries[i][0]
            if targetVal%2!=0 and changedVal%2==0:
                evenSum = evenSum + changedVal
                ans.append(evenSum)
            elif targetVal%2==0 and changedVal%2==0:
                evenSum = evenSum + queries[i][0]
                ans.append(evenSum)
            elif targetVal%2==0 and changedVal%2!=0:
                evenSum = evenSum - targetVal
                ans.append(evenSum)
            else:
                ans.append(evenSum)
        return ans            
