# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return helper(head)
        
def helper(head):
    if head!=None and head.next!=None:
        temp = head.next 
        head.next = helper(temp.next)
        temp.next = head
        return temp
    return head
