class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def sortFunction(log):
            primary,secondary = log.split(" ",1)
            return (0,secondary,primary) if secondary[0].isalpha() else(1,)
        
        return sorted(logs, key = sortFunction)
