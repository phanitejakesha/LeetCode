# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helperCount(root)
        
        
        
    def helperCount(self,root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return self.helperCount(root.right) + 1
        elif root.right is None:
            return self.helperCount(root.left) + 1
        else:
            return self.helperCount(root.left) + self.helperCount(root.right) + 1
    
