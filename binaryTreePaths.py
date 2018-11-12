#Leetcode problem Number 257
#Binary Tree Paths

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.ans=[]
        self.path(root,'')
        return self.ans
        
    def path(self,root,givenPath):
        if root is None:
            return 
        if root.left is None and root.right is None:
            self.ans.append(givenPath+str(root.val))
        self.path(root.left,givenPath+str(root.val)+'->')
        self.path(root.right,givenPath+str(root.val)+'->')
