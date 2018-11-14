#Leetcode problem Number 129
#sum root to leaf numbers


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=[]
        self.path(root,'')
        res = 0
        for i in range(0,len(self.ans)):
            res+=int(self.ans[i])
        return res
        
    def path(self,root,givenPath):
        if root is None:
            return 
        if root.left is None and root.right is None:
            self.ans.append(givenPath+str(root.val))
        self.path(root.left,givenPath+str(root.val))
        self.path(root.right,givenPath+str(root.val))
