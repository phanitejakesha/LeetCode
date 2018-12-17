#Leetcode Question Number 92
#Reverse Linked List


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        li =[]
        temp = head
        temp1 = head
        while temp!=None:
            li.append(temp.val)
            temp =temp.next
        reverse = li[:m-1]+li[m-1:n][::-1]+li[n:]
        while temp1!=None:
            temp1.val = reverse.pop(0)
            temp1=temp1.next 
        return head
        
