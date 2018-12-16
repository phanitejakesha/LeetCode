#Leetcode problem Number 589
#N-ary Tree Pre Order traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        ans =[]
        self.ITrans(root,ans)
        return ans
    
    
    def ITrans(self, root,ans):
        if root is None:
            return [] 
        ans.append(root.val)
        for i in range(0,len(root.children)):
            self.ITrans(root.children[i],ans)
        


