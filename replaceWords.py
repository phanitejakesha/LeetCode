class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if len(dict)==0:
            return sentence
        sList = set()
        for key in dict:
            sList.add(key)

        res = []       
        splitSentence = sentence.split()
        for i in range(0,len(splitSentence)):
            for j in range(0,len(splitSentence[i])):
                flag = True
                if splitSentence[i][0:j] in sList:
                    res.append(splitSentence[i][0:j])
                    flag = False
                    break
            if flag == True:
                res.append(splitSentence[i])
        return ' '.join(res)
        
        
