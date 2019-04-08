# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda K:K.start)
        if len(intervals)<2:
            return 0
        endVal = intervals[0].end
        count = 0 
        for i in range(1,len(intervals)):
            if endVal > intervals[i].start:
                count+=1
                endVal = min(endVal,intervals[i].end)
            else:
                endVal = intervals[i].end
        return count
        
        
        
        
        
        
      
