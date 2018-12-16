#Leetcode problem Number 938
#Range sum of BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.ans = 0 
        self.L = L
        self.R  = R
        self.ITrans(root,self.ans)
        return self.ans
    
    
    def ITrans(self, root,ans):
        if root is None:
            return 
        self.ITrans(root.left,self.ans)
        if root.val>=self.L and root.val<=self.R:
            self.ans+=root.val
        self.ITrans(root.right,self.ans)


