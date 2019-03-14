class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordDict = set()
        for word in words:
            wordDict.add(word)
        res = ""
        for key in wordDict:
            count = 0
            for i in range(1,len(key)+1):
                if key[0:i] in wordDict:
                    count+=1
            if count == len(key) and count>len(res):
                res = key
            elif count == len(res) and count == len(key):
                if res > key:
                    res = key
        return res
