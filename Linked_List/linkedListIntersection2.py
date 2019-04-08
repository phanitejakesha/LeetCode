# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        nodeHash = set()
        temp = head
        while head!=None:
            if head in nodeHash:
                return head
            else:
                nodeHash.add(head)
            head = head.next
        return None
             
