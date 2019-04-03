# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #since n is always valid 
        #find length of the linked list 

        lenOfList = 0
        temp = head
        while temp!=None:
            temp  = temp.next 
            lenOfList+=1
        if lenOfList == n:
            return head.next
        i = 0 
        temp2 = head
        while i < (lenOfList-n):
            if i == (lenOfList-n-1):
                head.next = head.next.next
            else:
                head = head.next
            i+=1
            
        return temp2
            
            
        
            
