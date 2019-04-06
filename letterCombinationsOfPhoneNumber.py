class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapSet = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        newResult = []
        for i in range(0,len(digits)):
            if i == 0 :
                newResult = list(mapSet[digits[i]])
            else:
                interM = []
                for each in newResult: 
                    sResult = list(mapSet[digits[i]])
                    for k in sResult:
                        interM.append(each+k)
                newResult = interM
        return newResult



