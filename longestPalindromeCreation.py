class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        #greedy solution, checking all pairs and one center atmost is possible since it should be a palindrome 
        ans = 0 
        listOfLetters = collections.Counter(s)
        values = listOfLetters.values()
        boolValue = True
        for value in values:
            ans+=(value//2)*2
            if value%2!=0 and boolValue == True:
                ans+=1
                boolValue = False
        return ans
    
    
