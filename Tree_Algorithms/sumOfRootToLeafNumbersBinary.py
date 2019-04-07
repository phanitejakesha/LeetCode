# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=[]
        self.path(root,'')
        result = 0
        for i in range(0,len(self.ans)):
            result+=int(self.ans[i],2)
        x = 10**9 + 7
        y = result%x
        return y
            
        
    def path(self,root,givenPath):
        if root is None:
            return 
        if root.left is None and root.right is None:
            self.ans.append(givenPath+str(root.val))
        self.path(root.left,givenPath+str(root.val))
        self.path(root.right,givenPath+str(root.val))
        
