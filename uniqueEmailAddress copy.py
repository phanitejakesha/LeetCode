#Leetcode problem Number 794
#valid tic tac toe state 

from collections import Counter
class Solution:
    def two_winners(self,full_board):
            if full_board[0]==full_board[1]==full_board[2] and full_board[6]==full_board[7]==full_board[8] and full_board[0]!=' ':
                return False
            if full_board[0]==full_board[1]==full_board[2] and full_board[3]==full_board[4]==full_board[5] and full_board[0]!=' ':
                return False
            if full_board[3]==full_board[4]==full_board[5] and full_board[6]==full_board[7]==full_board[8] and full_board[3]!=' ':
                return False
            if full_board[0]==full_board[3]==full_board[6] and full_board[1]==full_board[4]==full_board[7] and full_board[0]!=' ':
                return False
            if full_board[0]==full_board[3]==full_board[6] and full_board[2]==full_board[5]==full_board[8] and full_board[0]!=' ':
                return False
            if full_board[2]==full_board[5]==full_board[8] and full_board[1]==full_board[4]==full_board[7] and full_board[2]!=' ':
                return False
            
    def winn_state(self,full_board):
            if full_board[0]==full_board[1]==full_board[2]:
                return full_board[0]
            if full_board[3]==full_board[4]==full_board[5]:
                return full_board[3]
            if full_board[6]==full_board[7]==full_board[8]:
                return full_board[6]
            if full_board[0]==full_board[4]==full_board[8]:
                return full_board[0]
            if full_board[2]==full_board[4]==full_board[6]:
                return full_board[2]
            if full_board[0]==full_board[3]==full_board[6]:
                return full_board[0]
            if full_board[1]==full_board[4]==full_board[7]:
                return full_board[1]
            if full_board[2]==full_board[5]==full_board[8]:
                return full_board[2]
            
    def validTicTacToe(self, board):
            """
            :type board: List[str]
            :rtype: bool
            """
            full_board=board[0]+board[1]+board[2]
            d=Counter(full_board)
            if d[' ']==9:
                return True
            if d['X']==1 and d[' ']==8:
                return True
            if 'O' in d.keys() and 'X' in d.keys():
                if d['X']<d['O']:
                    return False
                if d['X']-d['O']>1:
                    return False
            elif 'O' in d.keys():
                return False
            elif 'X' in d.keys() and d['X']>1:
                return False
            x= self.two_winners(full_board)
            if x==False:
                return False
            y=self.winn_state(full_board)
            if y=='X':
                if d['O']+1!=d['X']:
                    return False
            if y=='O':
                if d['O']+d['X']==9:
                    return False
                if d['O']!=d['X']:
                    return False
            return True
    
            
