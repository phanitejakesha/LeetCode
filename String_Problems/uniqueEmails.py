#Leetcode problem Number 929
#unique email addresses

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d = set()
        for i in range(0,len(emails)):
            domainName =emails[i].split('@')[1] 
            userName = emails[i].split('@')[0]
            userName = userName.split('+')[0]
            userName = userName.split('.')
            uName = ''.join(userName)
            finalEmail = uName + "@"+domainName
            if finalEmail not in d:
                d.add(finalEmail)
        return len(d)
        
