#Leetcode Question Number 144
#Binary tree preorder traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.li = []
        self.preorder(root,self.li)
        return self.li
    
    
    def preorder(self,root,li):
        if root is None:
            return 
        self.li.append(root.val)
        self.preorder(root.left,li)
        self.preorder(root.right,li)
