class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        x = str(bin(N))[2:]
        c = []
        for i in range(0,len(x)):
            if x[i]=='1':
                c.append('0')
            else:
                c.append('1')
        s = ''.join(c)
        return int(s, 2)
