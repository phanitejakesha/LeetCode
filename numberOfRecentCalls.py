#Leetcode problem Number 933
#Number of recent calls

class RecentCounter(object):

    def __init__(self):
        self.li  = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.li.append(t)
        rangeMin = t-3000
        rangeMax = t
        ans = 0
        i = 0
        #print(t)
        while i <len(self.li):
            #print(self.li)
            #print(self.li[i],rangeMin,rangeMax)
            if self.li[i]>=rangeMin and self.li[i]<=rangeMax:
                return len(self.li)-i
            else:
                self.li.pop(i)
            
        return ans
        
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
