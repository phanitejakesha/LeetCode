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
        
        first = head
        second = head
        i = 0
        while i < n:
            second = second.next
            i+=1
        
        if second == None:
            return head.next
        
        
        while second.next!=None:
            second = second.next
            first = first.next
        first.next = first.next.next
        return head
            
