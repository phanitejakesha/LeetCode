#Leetcode problem Number 906
#super pallindromes

class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        p = generatePaldindromes(100)
        x = int(math.sqrt(int(L)))
        y = int(math.sqrt(int(R)))+1
        print(x,y)
        p = generatePaldindromes(y)
        ans = []
        for i in range(0,len(p)):
            if p[i]>=x:
                m = p[i]*p[i]
                if str(m)==str(m)[::-1]:
                    ans.append(m)
        return len(ans)
        

        
def createPalindrome(inp, b, isOdd): 
    n = inp 
    palin = inp 
   
    # checks if number of digits is odd or even 
    # if odd then neglect the last digit of input in 
    # finding reverse as in case of odd number of 
    # digits middle element occur once 
    if (isOdd): 
        n = n / b 
   
    # Creates palindrome by just appending reverse 
    # of number to itself 
    while (n > 0): 
        palin = palin * b + (n % b) 
        n = n / b 
    return palin 



def generatePaldindromes(n): 
    ans = []
    # Run two times for odd and even length palindromes 
    for j in range(2): 
        # Creates palindrome numbers with first half as i.  
        # Value of j decided whether we need an odd length 
        # of even length palindrome. 
        i = 1
        while (createPalindrome(i, 10, j % 2) < n): 
            ans.append(createPalindrome(i, 10, j % 2)) 
            i = i + 1
    return ans
