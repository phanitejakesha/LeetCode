class Solution:
    def queryString(self, S: str, N: int) -> bool:
        setOfStrings = set( self.get_all_substrings(S)) 
        for i in range(0,N+1):
            print(i)
            if str(bin(i)[2:]) not in setOfStrings:
                return False
        return True
        
        
        
    def get_all_substrings(self,input_string):
        length = len(input_string)
        return [input_string[i:j+1] for i in range(length) for j in                                        range(i,length)]
