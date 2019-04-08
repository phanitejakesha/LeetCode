# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        oddHead = head
        evenHead = even = head.next 
        while even!=None and even.next!=None:
            oddHead.next = even.next
            oddHead  = oddHead.next
            even.next = oddHead.next
            even = even.next
        oddHead.next = evenHead
        return head
        
