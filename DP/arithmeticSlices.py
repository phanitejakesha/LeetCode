#Leetcode problem Number 413
#Dynamic Programming
#Arithmetic Slices
"""
Author: Phani Teja Kesha
"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        i = 0
        stack = []
        ans = 0
        while i < len(A):
            #print(i)
            #print(stack)
            if i==0:
                stack.append(A[i])
            elif i==1:
                stack.append(A[i])
                diff = A[1]-A[0]
            else:
               # print(A[i])
                print(diff,A[i],stack[-1])
                if diff == A[i]-stack[-1]:
                    stack.append(A[i])
                else:
                    if len(stack)>=3:
                        ans += ((len(stack)-1)*(len(stack)-2)/2)
                    lastVal = stack[-1]
                    stack = []
                    stack.append(lastVal)
                    diff = A[i]-stack[-1]
                    stack.append(A[i])
            
            i+=1
        if len(stack)>=3:
            ans += ((len(stack)-1)*(len(stack)-2)/2)
        return ans
                
