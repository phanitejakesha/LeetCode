# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.ans = set()
        self.treeTraversal(root)
        for key in self.ans:
            if k-key in self.ans and (k-key)!=key:
                return True
        return False
        
    def treeTraversal(self,root):
        if root is None:
            return 
        self.treeTraversal(root.left)
        self.treeTraversal(root.right)
        self.ans.add(root.val)
        
