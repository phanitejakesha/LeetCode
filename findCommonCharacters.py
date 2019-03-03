class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        dic = {}
        for letter in A[0]:
            if letter in dic:
                dic[letter] += 1
            else:
                dic[letter] = 1
        if len(A) == 1:
            result = []
            for letter in A[0]:
                result.append(letter)
            return result
        for word in A[1:]:
            newDic = {}
            for letter in word:
                if letter in newDic:
                    newDic[letter] += 1
                else:
                    newDic[letter] = 1
            keys = list(dic.keys())
            # print(keys)
            for key in keys:
                if key in newDic:
                    dic[key] = min(dic[key], newDic[key])
                else:
                    del dic[key]
        result = []
        for key in dic:
            for i in range(dic[key]):
                result.append(key)
        return result
        
