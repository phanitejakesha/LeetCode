class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.data[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        ans = 0
        for key in self.data:
            if len(key)>=len(prefix):
                if key[:len(prefix)] == prefix:
                    ans  = ans +  self.data[key]
        return ans
                    


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
