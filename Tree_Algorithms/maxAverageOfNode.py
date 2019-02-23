# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAverageNode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.treeHelper(root)
    
    def treeHelper(self,root):
        if root.left is None and root.right is None:
            return root.val
        elif root.left is None:
            return max((self.treeHelper(root.right)+root.val)/2,root.right.val)
        elif root.right is None:
            return max((self.treeHelper(root.left)+root.val)/2,root.left.val)
        else:
            return max((self.treeHelper(root.left)+self.treeHelper(root.right)+root.val)/3,self.treeHelper(root.left),self.treeHelper(root.right))
