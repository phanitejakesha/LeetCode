class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        licensePlate =licensePlate.lower()
        isAlpha = set(list('abcdefghijklmnopqrstuvwxyz'))
        stVal = {}
        for i in range(0,len(licensePlate)):
            if licensePlate[i] in isAlpha:
                if licensePlate[i] in stVal:
                    stVal[licensePlate[i]]+=1
                else:
                    stVal[licensePlate[i]]=1
        
        ans = ""
        from collections import Counter
        for i in range(0,len(words)):
            boo = False
            li = Counter(words[i])
            for key in stVal:
                if key in li:
                    if stVal[key] <= li[key]:
                        continue
                    else:
                        boo = True
                else:
                    boo = True
            if boo == False:
                if ans == "":
                    ans = words[i]
                else:
                    if len(ans)> len(words[i]):
                        ans = words[i]
        return ans
        
        
            
            
            
