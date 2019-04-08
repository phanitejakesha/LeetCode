class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        from collections import Counter
        listOfPeople = Counter(ages)
        answer=0
        for key1 in listOfPeople:
            for key2 in listOfPeople:
                b1 = False
                b2 = False
                b3 = False
                if key2<=0.5*key1 + 7:
                    b1 = True
                if key2 > key1:
                    b2 = True
                if key2>100  and key1<100:
                    b3 = True 
                if b1==b2==b3==False:
                    if key1==key2 and listOfPeople[key1]==1:
                        pass
                    elif key1==key2 and listOfPeople[key1]>1 :
                        answer+=(listOfPeople[key1])*(listOfPeople[key1]-1)
                    else:
                        answer+= listOfPeople[key1]*listOfPeople[key2] 
        return answer
                    
                
        
