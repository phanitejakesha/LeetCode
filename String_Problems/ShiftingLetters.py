#Leetcode problem Number 848
#Shifting Letters 

class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        li = []
        su = 0
        ans = ""
        x = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        shifts.reverse()
        for i in range(0,len(shifts)):
            su = su + shifts[i]
            li.append(su)
        li.reverse()
        for i in range(0,len(S)):
            ans = ans + x[(li[i]+(ord(S[i])-97))%26] 
        return ans
            
        
