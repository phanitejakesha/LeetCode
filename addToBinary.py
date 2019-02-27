class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a)==0 and len(b)==0:
            return ""
        if len(a)!=len(b):
            if len(a)>len(b):
                b = ''.join(['0']*(len(a)-len(b))) +b
            else:
                a = ''.join(['0']*(len(b)-len(a)))+a
        c = 0
        ans = []
        for i in range(len(a)-1,-1,-1):
            s = int(a[i])+int(b[i]) + c
            if s == 3:
                ans.append('1')
                c = 1
            elif s == 2:
                ans.append('0')
                c = 1
            elif s == 1:
                ans.append('1')
                c = 0
            else:
                ans.append('0')
                c = 0 
        if c!=0:
            ans.append('1')
        return ''.join(ans)[::-1]
        
                
            
