#Leetcode 543
#diameter of a binary tree


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


dia = 0 
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def depth(root):
            if root is None:
                return 0
            Le = depth(root.left)
            Ri = depth(root.right)
            self.ans = max(self.ans,Le+Ri+1)
            return max(Le,Ri)+1
        depth(root)
        return self.ans-1
