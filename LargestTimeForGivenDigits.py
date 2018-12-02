#Leetcode problem Number 949
#largest Time for given digits

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        import itertools
        li = list(itertools.permutations(A))
        ans = []
        for key in li:
            hours = int(str(key[0])+str(key[1]))
            minutes = int(str(key[2])+str(key[3]))
            if hours<24 and minutes<60:
                hours = str(hours)
                minutes = str(minutes)
                if len(hours)==1:
                    hours ="0"+hours
                if len(minutes)==1:
                    minutes ="0"+minutes
                ans.append(str(hours)+":"+str(minutes))
        ans.sort()
        if len(ans)==0:
            return ""
        return str(ans[len(ans)-1])
                
                
