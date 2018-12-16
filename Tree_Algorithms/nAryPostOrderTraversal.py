#Leetcode problem Number 590
#N - ary postorder travsersal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        q = []
        q.append(root)
        ans = []
        while len(q)!=0:
            r = q.pop()
            ans.append(r.val)
            for i in r.children:
                q.append(i)
        return ans[::-1]
            
            
            
