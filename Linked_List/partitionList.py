# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        a = beforeList = ListNode(0)
        b = afterList = ListNode(0)
        while head!=None:
            if head.val < x:
                newNode = ListNode(head.val)
                beforeList.next = newNode
                beforeList = beforeList.next
            else:
                newNode = ListNode(head.val)
                afterList.next = newNode
                afterList = afterList.next
            head = head.next
        
        a = a.next
        b = b.next 
        temp = a
        if a == None:
            return b
        else:
            while a.next!=None:
                a  = a.next
        a.next = b
        return temp
            
