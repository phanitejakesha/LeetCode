# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.li = []
        self.inorder(root)
        self.result = {}
        for i in range(0,len(self.li)):
            self.result[self.li[i]] = sum(self.li[i:])
        self.changeTree(root)
        return root
        
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        self.li.append(root.val)
        self.inorder(root.right)
        
    def changeTree(self,root):
        if root is None:
            return 
        self.changeTree(root.left)
        root.val = self.result[root.val]
        self.changeTree(root.right)
        
