class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        li = []
        upperCasePattern = []
        for i in range(0,len(pattern)):
            if pattern[i].isupper():
                upperCasePattern.append(pattern[i])
            li.append(pattern[i])
            li.append('.*')
        li =''.join(li)
        ans = []
        for i in range(0,len(queries)):
            bool1 = bool(re.search(li, queries[i]))
            upperList = []
            for j in range(0,len(queries[i])):
                if queries[i][j].isupper():
                    upperList.append(queries[i][j])
            if len(upperList)!=len(upperCasePattern):
                 ans.append(False)
            else:
                for i in range(0,len(upperList)):
                    if upperList[i]!=upperCasePattern[i]:
                        bool1= False
                        break
                ans.append(bool1)    
        return ans
            
  
#         l = []
#         flag = False
#         for i in range(0,len(pattern)): 
#             if pattern[i].isupper():
#                 upperCasePattern.append(pattern[i])
#             if pattern[i].islower() and flag == True:
#                 l.append('*')            
#         l = ''.join(l)
#         ans = []
#         print(l)
#         for i in range(0,len(queries)):
#             bool1 = bool(re.search(l, queries[i]))
#             print(bool1)
#             upperList = []
#             for j in range(0,len(queries[i])):
#                 if queries[i][j].isupper():
#                     upperList.append(queries[i][j])
#             if len(upperList)!=len(upperCasePattern):
#                 ans.append(False)
#             else:
#                 for i in range(0,len(upperList)):
#                     if upperList[i]!=upperCasePattern[i]:
#                         bool1= False
#                         break
#                 ans.append(bool1)
#         return ans
            
            
        
