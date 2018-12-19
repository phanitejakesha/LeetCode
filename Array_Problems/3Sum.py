#Leetcode problem Number 15
#3 Sum
#Author : Phani Teja

class Solution(object):
    def addSum(self,li):
        li.sort()
        a=""
        for key in li:
            if key<0:
                a = a+"*"+str(abs(key))
            else:
                a=a+str(key)
        return a
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from collections import Counter
        d = Counter(nums)
        ans = []
        dStr = {}
        for key1 in d:
            x = -key1
            for key2 in d:
                if x-key2 in d:
                    key3 = x-key2
                    if key1!=key2 and key1!=key3 and key2!=key3:
                        li = [key1,key2,key3]
                        xx = self.addSum(li)
                        #print(xx)
                        if xx not in dStr:
                            dStr[xx]=1
                            ans.append(li)
                    elif key1==key2==key3:
                        if d[key1]>=3:
                            li = [key1,key2,key3]
                            xx = self.addSum(li)
                            #print(xx)
                            if xx not in dStr:
                                dStr[xx]=1
                                ans.append(li)
                    elif key1==key2:
                        if d[key1]>=2:
                            li = [key1,key2,key3]
                            xx = self.addSum(li)
                            #print(xx)
                            if xx not in dStr:
                                dStr[xx]=1
                                ans.append(li)
                    elif key1==key3:
                        if d[key1]>=2:
                            li = [key1,key2,key3]
                            xx = self.addSum(li)
                            #print(xx)
                            if xx not in dStr:
                                dStr[xx]=1
                                ans.append(li)
                    elif key3==key2:
                        if d[key2]>=2:
                            li = [key1,key2,key3]
                            xx = self.addSum(li)
                            #print(xx)
                            if xx not in dStr:
                                dStr[xx]=1
                                ans.append(li)
        return ans
                    
