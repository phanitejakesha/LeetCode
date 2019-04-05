# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.score = 0
        self.traversal(root)
        return self.score

    def traversal(self,root):
        if root is None:
            return 0
        leftVal = self.traversal(root.left)
        rightVal = self.traversal(root.right)
        self.score += abs(leftVal) + abs(rightVal)
        return root.val + leftVal + rightVal -1
        
