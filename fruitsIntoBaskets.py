#Leetcode problem Number 904
#Fruit into baskets

"""
Author: Phani Teja Kesha
"""

class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        index = 0
        flag = True
        result = []
        
        cnt = 0
        while(flag == True):
            b1 = -1
            b2 = -1
            #print(index)
            for i in range(index, len(tree)):
                if b1 == -1:
                    b1 = tree[i]
                    cnt += 1
                elif b1 == tree[i]:
                    cnt += 1
                else:
                    if b2 == -1:
                        b2 = tree[i]
                        index = i
                        cnt += 1
                    elif b2 == tree[i]:
                        cnt += 1
                    elif b2 != tree[i]:
                        result.append(cnt)
                        cnt = 0
                        break
            result.append(cnt)
            #print(i)
            if i == len(tree) -1:
                flag = False
        return max(result)
