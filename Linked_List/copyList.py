import copy 
        return copy.deepcopy(head)
        valueList = []
        nodeRandomList = []        
        while head!=None:
            valueList.append(head.val)
            nodeRandomList.append(head.random)
            head = head.next
        
        for i in range(0,len(valueList)):
            if i == 0:
                temp = Node(valueList[0],None,nodeRandomList[0])
                headNew = temp
            else:
                temp1 = Node(valueList[1],None,nodeRandomList[1])
                temp.next = temp1
                temp = temp1
        return headNew
