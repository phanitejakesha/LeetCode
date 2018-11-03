#Leetcode problem Number 532
#K - Different Pairs
"""
Author:Phani Teja Kesha

"""
class Solution(object):
    def createStr(self,k1,k2):
            li = [k1,k2]
            li.sort()
            st = ""
            if li[0]<0:
                st=st+"*"+str(abs(li[0]))
            else:
                st = st+str(abs(li[0]))
            if li[1]<0:
                st=st+"*"+str(abs(li[1]))
            else:
                st = st+str(abs(li[1]))
            return st
            
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        from collections import Counter
        numSet = Counter(nums)
        ansSet = set()
        for key in numSet:
            key2 = key+k
            key3 = key-k
            if key2 in numSet:
                if key==key2:
                    if numSet[key]>1:
                        st = self.createStr(key,key2)
                        ansSet.add(st)
                else:
                    st = self.createStr(key,key2)
                    ansSet.add(st)
            if key3 in numSet:
                if key==key3:
                    if numSet[key]>1:
                        st = self.createStr(key,key3)
                        ansSet.add(st)
                else:
                    st = self.createStr(key,key3)
                    ansSet.add(st)
        print(ansSet)
        return len(ansSet)
    
        
