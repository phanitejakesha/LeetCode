#Leetcode problem Number 112
#Path Sum

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.ans=set()
        self.path(root,0)
        if sum in self.ans:
            return True
        return False
        
    def path(self,root,givenPath):
        if root is None:
            return 
        if root.left is None and root.right is None:
            self.ans.add(givenPath+root.val)
        self.path(root.left,givenPath+root.val)
        self.path(root.right,givenPath+root.val)
