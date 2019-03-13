`class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        fRow = set("qwertyuiop")
        sRow = set("asdfghjkl")
        tRow = set("zxcvbnm")
        ans = []
        for word in words:
            if set(word.lower())<=fRow:
                ans.append(word)
            elif set(word.lower())<=sRow:
                ans.append(word)    
            elif set(word.lower())<=tRow:
                ans.append(word)
        return ans


