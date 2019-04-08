# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #hashmap solution 
        listA = set()
        while headA!= None:
            listA.add(headA)
            headA = headA.next
        while headB!=None:
            if headB in listA:
                return headB
            headB = headB.next
        return None
