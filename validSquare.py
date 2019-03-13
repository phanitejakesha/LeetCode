import math
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        import itertools
        x = list(itertools.permutations([1, 2, 3, 4]))
        for i in range(0,len(x)):
            a = self.convertNum(x[i][0],p1,p2,p3,p4)
            b = self.convertNum(x[i][1],p1,p2,p3,p4)
            c = self.convertNum(x[i][2],p1,p2,p3,p4)
            d = self.convertNum(x[i][3],p1,p2,p3,p4)
            if self.valid(a,b,c,d) == True:
                return True
        return False
           
    def valid(self,p1,p2,p3,p4):
        d1 = math.hypot(p2[0] - p1[0], p2[1] - p1[1])
        d2 = math.hypot(p2[0] - p3[0], p2[1] - p3[1])
        d3 = math.hypot(p3[0] - p4[0], p3[1] - p4[1])
        d4 = math.hypot(p4[0] - p1[0], p4[1] - p1[1])
        d5 = math.hypot(p2[0] - p4[0], p2[1] - p4[1])
        d6 = math.hypot(p1[0] - p3[0], p1[1] - p3[1])
        if d1==d2==d3==d4 and d5==d6 and d1!=0 and d5!=0:
            return True
        else:
            return False
        
    def convertNum(self,x,p1,p2,p3,p4):
        if x == 1:
            return p1
        elif x == 2:
            return p2
        elif x == 3:
            return p3
        return p4
