class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N==1:
            return 1
        hashValue = {}
        hashSet = set()
        for i in range(0,len(trust)):
            hashSet.add(trust[i][0])
            if trust[i][1] not in hashValue:
                hashValue[trust[i][1]] = set()
                hashValue[trust[i][1]].add(trust[i][0])
            else:
                hashValue[trust[i][1]].add(trust[i][0])
        for key in hashValue:
            if len(hashValue[key]) == N-1 and key not in hashSet:
                return key
        return -1
                
                
