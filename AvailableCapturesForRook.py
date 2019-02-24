class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        pawnLocation=self.findLoc(board)
        count = 0 
        for i in range(pawnLocation[0],-1,-1):
            if board[i][pawnLocation[1]]=='p':
                count+=1
                break
            elif board[i][pawnLocation[1]] == 'B':
                break
        for i in range(pawnLocation[0],8):
            if board[i][pawnLocation[1]]=='p':
                count+=1
                break
            elif board[i][pawnLocation[1]] == 'B':
                break
        for i in range(pawnLocation[1],-1,-1):
            if board[pawnLocation[0]][i]=='p':
                count+=1
                break
            elif board[pawnLocation[0]][i] == 'B':
                break
        for i in range(pawnLocation[1],8):
            if board[pawnLocation[0]][i]=='p':
                count+=1
                break
            elif board[pawnLocation[0]][i] == 'B':
                break
        return count   
        
                
    
    def findLoc(self,board):
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if board[i][j]=='R':
                    return [i,j]
        
        
        class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N==1:
            return 1
        hashValue = {}
        hashSet = set()
        for i in range(0,len(trust)):
            hashSet.add(trust[i][0])
            if trust[i][1] not in hashValue:
                hashValue[trust[i][1]] = set()
                hashValue[trust[i][1]].add(trust[i][0])
            else:
                hashValue[trust[i][1]].add(trust[i][0])
        for key in hashValue:
            if len(hashValue[key]) == N-1 and key not in hashSet:
                return key
        return -1
                
                
