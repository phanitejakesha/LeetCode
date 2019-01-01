#Leetcode problem Number 965
#Univalued Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    value = 0 
    ans = True
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        self.value = root.val 
        self.helperFunction(root)
        return self.ans
    def helperFunction(self,root):
        if root is None:
            return 
        self.helperFunction(root.left)
        if self.value!= root.val:
            self.ans = False
        self.helperFunction(root.right)
